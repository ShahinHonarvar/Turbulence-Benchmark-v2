def return_binary_or_hexa(t):
    a, b = (t[57], t[84])
    missing = set(range(a + 1, b)) - set(t[57 + 1:84])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]