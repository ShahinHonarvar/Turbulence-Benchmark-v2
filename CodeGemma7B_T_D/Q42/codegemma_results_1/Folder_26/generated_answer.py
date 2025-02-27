def prime_factors(l):
    return set((factor for i in l for factor in factors(i)))

def factors(n):
    X = set()
    i = 2
    while i * i <= n:
        if not n % i:
            n //= i
            X.add(i)
        i += 1
    if n > 1:
        X.add(n)
    return X