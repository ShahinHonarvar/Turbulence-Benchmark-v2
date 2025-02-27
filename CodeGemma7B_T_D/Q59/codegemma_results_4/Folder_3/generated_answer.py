def all_left_truncatable_prime(t):
    r = []
    for i in range(t[100]):
        a = str(i)
        b = t[0]
        if i == int(a[0]):
            b = b * int(a[0])
            if b in t[1:]:
                r.append(b)
    r.sort()
    return r