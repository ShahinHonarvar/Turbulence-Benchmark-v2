def find_original_set(a, b, c, d):
    s = set()
    if a:
        s = a
        s.update(b)
        s.update(c)
        s.update(d)
    else:
        s = b
        s.update(c)
        s.update(d)
    return s