def prime_factors(lst):

    def get_primes(n):
        primes = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                primes.append(i)
        if n > 1:
            primes.append(n)
        return set(primes)
    return get_primes(lst[63])