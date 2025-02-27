def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    s = sum(set(range(a + 1, b)) - set(t[450:906]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]