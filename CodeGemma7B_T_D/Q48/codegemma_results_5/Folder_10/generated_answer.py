def return_binary_or_hexa(t):
    a, b = (t[36], t[54])
    s = 0
    for x in range(a + 1, b):
        if x not in t[36:55]:
            s += x
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:].upper() if s else ''