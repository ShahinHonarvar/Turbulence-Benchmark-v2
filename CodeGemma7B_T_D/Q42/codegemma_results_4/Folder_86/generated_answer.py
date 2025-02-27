from math import sqrt

def prime_factors(lst):
    lst_194 = lst[194]
    lst_factors = []
    if lst_194 == 1:
        lst_factors.append(1)
        return set(lst_factors)
    for i in range(2, int(sqrt(lst_194)) + 1):
        while lst_194 % i == 0:
            lst_factors.append(i)
            lst_194 //= i
    if lst_194 > 1:
        lst_factors.append(lst_194)
    return set(lst_factors)