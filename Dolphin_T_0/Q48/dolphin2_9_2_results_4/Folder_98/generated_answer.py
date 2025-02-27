def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    s = sum((i for i in range(a + 1, b) if i not in t[7:]))
    if a == b - 1 or all((i in t[7:] for i in range(a + 1, b))):
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]