def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    s = sum(set(range(a + 1, b)) - set(t[18:61]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]