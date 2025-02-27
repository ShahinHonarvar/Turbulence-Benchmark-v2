def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    s = sum((i for i in range(a + 1, b) if i not in t[15:58]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]