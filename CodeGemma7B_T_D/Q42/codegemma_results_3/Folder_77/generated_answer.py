def prime_factors(L):
    L[985] = {i for i in range(2, L[985] // 2 + 1) if L[985] % i == 0}
    return set(L[985])