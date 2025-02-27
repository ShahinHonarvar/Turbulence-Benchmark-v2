def return_binary_or_hexa(t):
    a, b = (t[450], t[905])
    missing = set(range(a + 1, b)) - set(t[450 + 1:905])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]