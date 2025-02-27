def prime_factors(lst):

    def get_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    if 733 < len(lst):
        return get_prime_factors(lst[733])
    else:
        return set()