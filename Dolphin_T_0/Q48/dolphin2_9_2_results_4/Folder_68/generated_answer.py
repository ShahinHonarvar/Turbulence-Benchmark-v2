def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    s = sum(set(range(a + 1, b)) - set(t[1:10]))
    if s == 0:
        return ''
    r = bin(s) if s % 2 else hex(s)
    return r[2:] if s % 2 == 1 else r[2:].upper()