def prime_factors(factors):
    return set((factor for factor in factors[43] if factor in prime_factors(factors[:43])))