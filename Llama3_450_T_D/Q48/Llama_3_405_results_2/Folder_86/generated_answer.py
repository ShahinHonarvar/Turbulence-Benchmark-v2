def return_binary_or_hexa(t):
    a = t[19]
    b = t[32]
    s = sum((i for i in range(a + 1, b) if i not in t[20:32]))
    if s == 0:
        return ''
    elif s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]