def all_left_truncatable_prime(t):
    a = 23
    b = 10 ** (a - 2)
    c = b * a
    d = b ** (a - 1)
    e = c + d
    f = e - b
    g = b ** a
    h = f + g
    i = h - b
    return [h, i]