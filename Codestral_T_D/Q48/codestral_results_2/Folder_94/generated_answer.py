def return_binary_or_hexa(t):
    a, b = (t[42], t[87])
    missing = set(range(a + 1, b)) - set(t[42 + 1:87])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]