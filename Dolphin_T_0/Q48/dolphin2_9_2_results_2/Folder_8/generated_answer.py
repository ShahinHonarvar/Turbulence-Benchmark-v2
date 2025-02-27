def return_binary_or_hexa(t):
    a, b = (t[45], t[48])
    missing = set(range(a + 1, b)) - set(t[46:48])
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper() if s else ''