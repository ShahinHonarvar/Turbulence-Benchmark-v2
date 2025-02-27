def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    s = sum((i for i in range(a + 1, b) if i not in t[14:91]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]