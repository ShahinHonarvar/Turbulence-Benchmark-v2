def return_binary_or_hexa(t):
    a, *_, b = t
    vals = set(range(a + 1, b))
    vals = vals.difference(set(t))
    if not vals:
        return ''
    s = sum(vals)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]