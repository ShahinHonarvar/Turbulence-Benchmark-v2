def return_binary_or_hexa(t):
    a, b = (t[55], t[84])
    s = sum(set(range(a + 1, b)) - set(t[55:85]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()