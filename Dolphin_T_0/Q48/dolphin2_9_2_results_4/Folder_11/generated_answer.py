def return_binary_or_hexa(t):
    a, b = (t[48], t[76])
    if all((x in t for x in range(a + 1, b))):
        return ''
    s = sum((x for x in range(a + 1, b + 1) if x not in t))
    if s % 2 == 0:
        return hex(s)[2:].upper()
    return bin(s)[2:]