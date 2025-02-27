def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    s = sum((i for i in range(a + 1, b) if i not in t[36:53]))
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]