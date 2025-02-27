def prime_factors(lst):

    def primes(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if 247 < len(lst):
        return primes(lst[247])
    return set()