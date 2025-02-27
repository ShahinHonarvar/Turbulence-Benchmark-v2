def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    s = sum((i for i in range(a + 1, b) if i not in t[21:51]))
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]