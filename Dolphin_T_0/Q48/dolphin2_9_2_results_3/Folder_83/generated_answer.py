def return_binary_or_hexa(t):
    a = t[90]
    b = t[200]
    s = sum((i for i in range(a + 1, b) if i not in t))
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]