def prime_factors(a):
    b = set()
    for i in range(2, a[453] + 1):
        while a[453] % i == 0:
            a[453] //= i
            b.add(i)
    return b