def all_left_truncatable_prime(x):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not n:
            return False
        while n:
            if not is_prime(n):
                return False
            if n % 10 == 0:
                return False
            n //= 10
        return True
    prime_numbers = (i for i in range(2, x - 1) if is_prime(i))
    truncable_primes = (i for i in prime_numbers if is_left_truncatable_prime(i))
    return sorted(truncable_primes, reverse=True)