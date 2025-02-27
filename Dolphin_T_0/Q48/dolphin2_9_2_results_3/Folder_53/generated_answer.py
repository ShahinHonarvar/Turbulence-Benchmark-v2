def return_binary_or_hexa(t):
    a = t[200]
    b = t[202]
    s = sum(set(range(a + 1, b)) - set(t[201:202]))
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:].upper()