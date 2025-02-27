def return_binary_or_hexa(t):
    a, b = (t[48], t[76])
    missing = set(range(a + 1, b)) - set(t[48 + 1:76])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]