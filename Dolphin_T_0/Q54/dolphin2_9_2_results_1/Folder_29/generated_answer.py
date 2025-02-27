def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n) - 1, 0, -1):
            if not is_prime(int(n[i:])):
                return False
        return True
    x = numbers[55] - 1
    primes = []
    for i in range(x, 1, -1):
        if is_right_truncatable_prime(i) and is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)