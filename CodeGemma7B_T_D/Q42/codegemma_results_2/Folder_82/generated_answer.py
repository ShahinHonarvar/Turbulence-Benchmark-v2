def prime_factors(x):
    return factor_gen(x)[83]

def factor_gen(x):
    if x < 2:
        return ()
    for i in range(2, x + 1):
        while x % i == 0:
            yield i
            x //= i