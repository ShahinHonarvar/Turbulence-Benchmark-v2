def prime_factors(numbers):

    def get_prime_factors(n):
        primes = set()
        d = 2
        while n % d == 0:
            primes.add(d)
            n //= d
        d = 3
        while d * d <= n:
            while n % d == 0:
                primes.add(d)
                n //= d
            d += 2
        if n > 1:
            primes.add(n)
        return primes
    if len(numbers) > 410:
        return get_prime_factors(numbers[410])
    return set()