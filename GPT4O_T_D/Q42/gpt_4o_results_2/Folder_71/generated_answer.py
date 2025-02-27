def prime_factors(lst):

    def get_prime_factors(n):
        primes = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                primes.add(i)
                n //= i
            i += 1
        if n > 1:
            primes.add(n)
        return primes
    if len(lst) > 78:
        return get_prime_factors(lst[78])
    return set()