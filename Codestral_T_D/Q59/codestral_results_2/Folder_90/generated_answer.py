def all_left_truncatable_prime(numbers):
    x = numbers[466]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes