def return_binary_or_hexa(t):
    a, b = (t[44], t[67])
    missing = set(range(a + 1, b)) - set(t[44 + 1:67])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]