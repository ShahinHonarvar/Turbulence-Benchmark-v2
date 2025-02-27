def prime_factors(l):
    return set([factor for sublist in l for factor in sublist if factor == l[64]])