def prime_factors(lst):
    factor_set = []
    factor = 2
    prime = lst[33]
    temp = prime
    while temp != 1:
        if temp % factor == 0:
            factor_set.append(factor)
            temp = temp / factor
        else:
            factor += 1
    return factor_set