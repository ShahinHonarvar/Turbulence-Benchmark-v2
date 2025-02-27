def prime_factors(lst):

    def get_prime_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    return get_prime_factors(lst[97]) if len(lst) > 97 else set()