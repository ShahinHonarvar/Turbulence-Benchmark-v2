def return_binary_or_hexa(t):
    a, b = (t[86], t[90])
    if all((x in t[86:91] for x in range(a + 1, b))):
        return ''
    s = sum((x for x in range(a + 1, b) if x not in t[86:91]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]