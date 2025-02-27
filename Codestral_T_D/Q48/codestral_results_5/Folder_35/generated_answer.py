def return_binary_or_hexa(t):
    a = t[77]
    b = t[84]
    missing = set(range(a + 1, b)) - set(t[77 + 1:84])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]