def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    s = sum((i for i in range(a + 1, b) if i not in t[8:9]))
    if s == 0:
        return ''
    elif s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]