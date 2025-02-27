def return_binary_or_hexa(t):
    a, b = (t[80], t[200])
    s = sum((x for x in range(a + 1, b) if x not in t[80:200]))
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''