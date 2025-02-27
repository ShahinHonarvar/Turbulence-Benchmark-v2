def return_binary_or_hexa(t):
    a, b = (t[0], t[3])
    s = sum((i for i in range(a + 1, b) if i not in t[:4]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]