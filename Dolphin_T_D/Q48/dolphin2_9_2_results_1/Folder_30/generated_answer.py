def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    s = sum((i for i in range(a + 1, b) if i not in t))
    if s % 2:
        if s == 0:
            return ''
        else:
            return bin(s)[2:]
    elif s == 0:
        return ''
    else:
        return hex(s)[2:]