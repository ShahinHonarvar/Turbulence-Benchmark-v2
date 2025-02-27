def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    s = sum((i for i in range(a + 1, b) if i not in t[38:43]))
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]