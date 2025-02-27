def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    s = sum(t[36:53])
    c = set(range(a + 1, b)) - set(t[36:53])
    d = sum(c)
    if d % 2 == 1:
        return bin(d)[2:]
    else:
        return hex(d)[2:].upper()