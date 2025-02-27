def prime_factors(l):
    num = l[733]
    primes = set()
    d = 2
    while d * d <= num:
        if num % d:
            d += 1
        else:
            num //= d
            primes.add(d)
    if num > 1:
        primes.add(num)
    return primes