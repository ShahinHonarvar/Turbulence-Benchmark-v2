def all_right_truncatable_prime(numbers):
    x = numbers[49]

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_right_truncatable(n // 10)
    primes = [n for n in range(2, x) if is_prime(n)]
    right_truncatable_primes = [p for p in primes if is_right_truncatable(p)]
    return sorted(right_truncatable_primes)