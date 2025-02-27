def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[89]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)