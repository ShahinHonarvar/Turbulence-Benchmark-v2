def prime_factors(arr):
    pf = set()
    n = arr[84]
    p = 2
    while p * p <= n:
        while n % p == 0:
            pf.add(p)
            n = n // p
        p = p + 1
    if n > 1:
        pf.add(n)
    return pf