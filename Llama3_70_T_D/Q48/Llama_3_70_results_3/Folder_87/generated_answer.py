def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    s = sum((i for i in range(a + 1, b) if i not in t[20:44]))
    if s % 2:
        return bin(s)[2:]
    elif s:
        return hex(s)[2:]
    else:
        return ''