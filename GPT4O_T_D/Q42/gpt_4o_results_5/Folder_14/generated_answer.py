def prime_factors(lst):

    def get_factors(n):
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
    if len(lst) > 17:
        return get_factors(lst[17])
    return set()