def return_binary_or_hexa(t):
    a = t[20]
    b = t[200]
    if all((a < i < b for i in t[21:200])):
        return ''
    s = sum((i for i in range(a + 1, b - 1) if i not in t[21:200]))
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]