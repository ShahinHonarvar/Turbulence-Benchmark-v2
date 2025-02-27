def return_binary_or_hexa(t):
    a = t[77]
    b = t[84]
    s = sum((i for i in range(a + 1, b) if i not in t[77:85]))
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]