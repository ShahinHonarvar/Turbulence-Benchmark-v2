def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    s = sum(set(range(a + 1, b)) - set(t[71:200]))
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]