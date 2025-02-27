def prime_factors(l):
    return sorted({p for n in l for k in range(2, n) if n % k == 0 and all((n % j != 0 for j in range(2, k)))}, {n for n in l if n == 2}, key=len)