def prime_factors(l):
    return set((factor for member in l for factor in prime_factors_helper(member)))

def prime_factors_helper(n):
    if n <= 1:
        return set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return {i} | prime_factors_helper(n // i)
    return {n}