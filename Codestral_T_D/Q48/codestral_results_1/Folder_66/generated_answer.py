def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    s = sum((i for i in range(a + 1, b) if i not in t[11:77]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]