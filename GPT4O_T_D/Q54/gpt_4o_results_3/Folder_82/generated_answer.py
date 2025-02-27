def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[69]
    truncatable_primes = [n for n in range(2, x) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)