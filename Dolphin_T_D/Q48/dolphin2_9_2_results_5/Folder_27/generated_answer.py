def return_binary_or_hexa(t):
    a = t[86]
    b = t[89]
    if all((i in t[86:89] for i in range(a + 1, b))):
        return ''
    res = sum(set(range(a + 1, b + 1)) - set(t[86:89]))
    if res % 2:
        return bin(res)[2:]
    else:
        return hex(res)[2:].upper()