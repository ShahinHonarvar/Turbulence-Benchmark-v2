def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    if all((i in t[57:86] for i in range(a + 1, b))):
        return ''
    s = sum((i for i in range(a + 1, b + 1) if i not in t[57:86]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]