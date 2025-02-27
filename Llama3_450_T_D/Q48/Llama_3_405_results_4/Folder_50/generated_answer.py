def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    s = sum((i for i in range(a + 1, b) if i not in t[14:76]))
    if s == 0:
        return ''
    elif s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]