def return_binary_or_hexa(t):
    a, b = (t[13], t[76])
    missing = set(range(a + 1, b)) - set(t[13:76])
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()