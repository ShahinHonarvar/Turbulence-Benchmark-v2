def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    m = set(t[1:4])
    s = sum(set(range(a + 1, b)) - m)
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]