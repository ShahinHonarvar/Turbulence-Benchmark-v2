def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    s = sum((x for x in range(a + 1, b) if x not in t[20:44]))
    if s % 2 == 1:
        return bin(s)[2:]
    elif s != 0:
        return hex(s)[2:]
    else:
        return ''