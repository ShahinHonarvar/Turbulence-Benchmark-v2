def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[91]
    left_truncatable_primes = []
    for num in range(2, x):
        digit_remover = lambda n: int(str(n)[1:])
        if all((is_prime(i) and digit_remover(i) != 0 for i in map(digit_remover, str(num)))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)