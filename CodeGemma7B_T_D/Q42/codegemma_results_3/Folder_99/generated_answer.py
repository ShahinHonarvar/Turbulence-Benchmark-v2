def prime_factors(lst):
    pf = set()
    n = lst[733]
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            pf.add(i)
            n //= i
    if n > 1:
        pf.add(n)
    return pf