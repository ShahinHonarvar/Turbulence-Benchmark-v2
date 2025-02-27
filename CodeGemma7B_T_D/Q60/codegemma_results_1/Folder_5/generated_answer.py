def all_left_right_truncatable_prime(y):
    h = min(y)
    i = max(y) if h <= 2 else h + 2
    o, p = (2, [])
    while i <= y:
        m, n, f = (i, int(str(i)[::-1]), True)
        while m > 1:
            if m % o == 0:
                f = False
                break
            o += 1
            if n > 1:
                if n % o == 0:
                    f = False
                    break
                o += 1
            m //= 10
            n //= 10
        if f:
            p.append(i)
        i += 1
    return sorted(p) if p else []