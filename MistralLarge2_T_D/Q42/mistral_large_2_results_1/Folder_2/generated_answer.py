def prime_factors(lst):

    def get_prime_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if len(lst) > 702:
        return get_prime_factors(lst[702])
    else:
        return set()