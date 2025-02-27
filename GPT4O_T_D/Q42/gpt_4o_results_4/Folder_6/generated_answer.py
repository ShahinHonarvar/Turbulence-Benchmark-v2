def prime_factors(lst):

    def get_prime_factors(n):
        factors = set()
        div = 2
        while n > 1:
            while n % div == 0:
                factors.add(div)
                n //= div
            div += 1
        return factors
    if len(lst) > 790:
        return get_prime_factors(lst[790])
    return set()