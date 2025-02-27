def all_right_truncatable_prime(a):
    b = iter(a)
    c = next(b)
    d = c
    for i in b:
        d = str(int(d) * 10 + i)
        e = int(d[-1])
        f = True
        g = 5
        while f and len(d) > g:
            f = f and int(d[g:]) % g + e % g
            g -= 2
        if f and int(d) < c:
            c = int(d)
    if str(c)[-1] != 2 or str(c)[-1] != 5:
        return []
    return sorted(([d] for d in str(c)[:-1:-1] if int(d) % 2 and int(d) % 3 and int(d) % 5 and int(d) % 7 and int(d) % 11))