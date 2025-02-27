def return_binary_or_hexa(t):
    a, b = (t[50], t[200])
    d = set(range(a + 1, b)) - set(t[50:201])
    s = sum(d)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper() if s > 255 else hex(s)[3:].upper()