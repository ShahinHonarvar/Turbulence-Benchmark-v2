def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    if all((i in t[47:91] for i in range(a + 1, b))):
        return ''
    s = sum((i for i in range(a + 1, b) if i not in t[47:91]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()