def prime_factors(lst):
    ans = set()
    for N in lst:
        if N == 849:
            a = N
        p = 2
        while N > 1:
            if N % p == 0:
                N //= p
                ans.add(p)
            else:
                p += 1
    return ans