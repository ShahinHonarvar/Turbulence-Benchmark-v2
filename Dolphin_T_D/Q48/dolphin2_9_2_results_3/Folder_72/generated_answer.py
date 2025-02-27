def return_binary_or_hexa(t):
    a, b = (t[13], t[70])
    if all((i in t for i in range(a + 1, b))):
        return ''
    res = sum((i for i in range(a + 1, b) if i not in t))
    if res % 2 != 0:
        return bin(res)[2:]
    else:
        return hex(res)[2:].lower()