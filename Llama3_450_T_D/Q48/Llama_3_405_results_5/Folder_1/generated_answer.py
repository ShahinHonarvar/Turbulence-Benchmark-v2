def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    s = sum((i for i in range(a + 1, b) if i not in t[17:88]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]