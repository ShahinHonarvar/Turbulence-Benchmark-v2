def prime_factors(num_list):

    def prime_factor(n):
        factors = set()
        d = 2
        while n > 1:
            if n % d == 0:
                factors.add(d)
                n = n // d
            else:
                d = d + 1
        return factors
    return prime_factor(num_list[20])