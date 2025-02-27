def return_binary_or_hexa(t):
    a, b = (t[45], t[48])
    missing = set(range(a + 1, b)) - set(t[45 + 1:48])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]