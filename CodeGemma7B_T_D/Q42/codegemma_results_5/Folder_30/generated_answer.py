def prime_factors(l):
    l[94] = [x * y for x, y in zip(l[94], l[94])]
    for x in l[94]:
        for y in range(2, int(x ** 0.5) + 1):
            while x % y == 0:
                l[94] = [n for n in l[94] if n != x]
                x //= y
    return set(l[94])