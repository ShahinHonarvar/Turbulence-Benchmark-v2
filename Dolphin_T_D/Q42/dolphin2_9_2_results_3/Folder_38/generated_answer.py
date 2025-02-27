def prime_factors(l):
    num = l[38]
    res = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            res.add(i)
    if num > 1:
        res.add(num)
    return res