def prime_factors(lst):

    def factors(n):
        i = 2
        fctrs = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                fctrs.add(i)
        if n > 1:
            fctrs.add(n)
        return fctrs
    return factors(lst[74])