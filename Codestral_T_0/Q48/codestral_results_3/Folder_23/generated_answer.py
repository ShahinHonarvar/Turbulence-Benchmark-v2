def return_binary_or_hexa(t):
    a, b = (t[20], t[36])
    missing = set(range(a + 1, b)) - set(t[20 + 1:36])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]