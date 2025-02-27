def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    missing = set(range(a + 1, b)) - set(t[6:7])
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]