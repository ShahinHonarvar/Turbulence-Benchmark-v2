def all_right_truncatable_prime(numbers):
    x = numbers[175]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable(n)]
    return sorted(right_truncatable_primes)