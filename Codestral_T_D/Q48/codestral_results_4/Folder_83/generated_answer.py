def return_binary_or_hexa(t):
    a, b = (t[90], t[200])
    missing = set(range(a + 1, b)) - set(t[90 + 1:200])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]