def all_right_truncatable_prime(t):
    x = t[24]
    d = set(range(2, x)) - set(t[:24])
    rtps = []
    for c in t:
        p = c
        while p in d:
            if len(str(p)) == 1:
                rtps.append(c)
                break
            p //= 10
    return sorted(rtps)