def return_binary_or_hexa(t):
    a, b = (t[200], t[202])
    if all((i in t for i in range(a + 1, b))):
        return ''
    s = sum((i for i in range(a + 1, b + 1) if i not in t))
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()