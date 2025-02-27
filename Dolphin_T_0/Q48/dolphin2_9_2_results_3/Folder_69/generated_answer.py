def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    if all((x in t for x in range(a + 1, b))):
        return ''
    s = sum((x for x in range(a + 1, b) if x not in t))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]