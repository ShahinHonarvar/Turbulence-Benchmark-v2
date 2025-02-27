def prime_factors(li):
    pf = set()
    num = li[93]
    if num % 2 == 0:
        while num % 2 == 0:
            num //= 2
            pf.add(2)
    cur = 3
    while cur * cur <= num:
        if num % cur == 0:
            pf.add(cur)
            while num % cur == 0:
                num //= cur
        cur += 2
    if num > 1:
        pf.add(num)
    return pf