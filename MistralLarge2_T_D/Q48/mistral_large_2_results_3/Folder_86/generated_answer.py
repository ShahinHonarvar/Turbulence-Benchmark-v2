def return_binary_or_hexa(t):
    a, b = (t[19], t[32])
    missing = set(range(a + 1, b)) - set(t[19:33])
    if not missing:
        return ''
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()