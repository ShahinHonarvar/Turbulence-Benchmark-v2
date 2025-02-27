def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    s = sum(range(a + 1, b)) - sum(t[40:43])
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]