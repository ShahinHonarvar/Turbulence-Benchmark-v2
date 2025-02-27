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

    def is_right_truncatable_prime(p):
        while p > 0:
            if not is_prime(p):
                return False
            p //= 10
        return True
    x = numbers[43]
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes)