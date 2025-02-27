def all_left_truncatable_prime(t):

    def is_truncatable_prime(n):
        if n < 2:
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n % 2 == 0:
            return n == 2
        sqr = int(n ** 0.5)
        for i in range(3, sqr + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[0]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = [i for i in primes if is_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)