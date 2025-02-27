def return_binary_or_hexa(t):
    a, b = (t[15], t[57])
    missing = set(range(a + 1, b)) - set(t[15 + 1:57])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]