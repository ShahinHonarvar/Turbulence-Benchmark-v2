def return_binary_or_hexa(t):
    a, b = (t[56], t[90])
    missing = set(range(a + 1, b)) - set(t[57:90])
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()