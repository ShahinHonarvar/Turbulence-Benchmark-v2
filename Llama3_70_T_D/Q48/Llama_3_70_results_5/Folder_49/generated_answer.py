def return_binary_or_hexa(t):
    a, b = (t[80], t[200])
    s = sum((i for i in range(a + 1, b) if i not in t[81:200]))
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]