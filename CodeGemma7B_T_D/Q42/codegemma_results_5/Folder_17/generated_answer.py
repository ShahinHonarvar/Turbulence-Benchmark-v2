def prime_factors(lst):
    factors = set()
    for i in lst:
        if i == lst[632]:
            for j in range(2, int(lst[632] ** 0.5) + 1):
                while lst[632] % j == 0:
                    factors.add(j)
                    lst[632] /= j
    return factors