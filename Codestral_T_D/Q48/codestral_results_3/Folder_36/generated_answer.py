def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    s = sum((i for i in range(a + 1, b) if i not in t[110:349]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]