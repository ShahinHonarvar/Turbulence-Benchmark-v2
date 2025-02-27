def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    s = sum((i for i in range(a + 1, b) if i not in t[61:200]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]