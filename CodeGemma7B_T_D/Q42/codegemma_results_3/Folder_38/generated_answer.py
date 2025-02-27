def prime_factors(lst):
    ans = set()
    for i in lst:
        for j in range(2, int(i ** 0.5) + 1):
            while i % j == 0:
                ans.add(j)
                i //= j
    return ans