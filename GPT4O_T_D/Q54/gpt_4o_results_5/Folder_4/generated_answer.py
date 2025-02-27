def all_right_truncatable_prime(numbers):
    x = numbers[96]

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            n //= 10
            if n > 0 and (not is_prime(n)):
                return False
        return True
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)