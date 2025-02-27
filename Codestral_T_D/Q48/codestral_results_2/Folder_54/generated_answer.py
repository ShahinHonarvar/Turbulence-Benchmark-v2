def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    missing = set(range(a + 1, b)) - set(t[35 + 1:64])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]