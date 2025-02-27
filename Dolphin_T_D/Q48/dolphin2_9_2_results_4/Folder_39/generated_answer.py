def return_binary_or_hexa(t):
    a = t[44]
    b = t[91]
    o = set(range(a + 1, b))
    a = set(t[44:92])
    o = o - a
    if len(o) == 0:
        return ''
    s = sum(o)
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]