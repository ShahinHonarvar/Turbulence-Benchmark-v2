def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    s = sum((i for i in range(a + 1, b) if i not in t[23:24]))
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]