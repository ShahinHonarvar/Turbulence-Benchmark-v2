def prime_factors(lst):

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

    def get_prime_factors(n):
        primes = set()
        while n % 2 == 0:
            primes.add(2)
            n //= 2
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                if is_prime(factor):
                    primes.add(factor)
                n //= factor
            factor += 2
        if n > 2:
            primes.add(n)
        return primes
    if len(lst) <= 56:
        return set()
    return get_prime_factors(lst[56])