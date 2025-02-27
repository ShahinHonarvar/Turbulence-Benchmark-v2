def find_original_set(a, b, c, d, e, f, g, h):
    s = a | b | c | d | e | f | g | h
    if a & s == a:
        return a
    if b & s == b:
        return b
    if c & s == c:
        return c
    if d & s == d:
        return d
    if e & s == e:
        return e
    if f & s == f:
        return f
    if g & s == g:
        return g
    if h & s == h:
        return h
    return s