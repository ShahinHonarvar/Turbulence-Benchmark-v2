def return_binary_or_hexa(t):
    a = t[86]
    b = t[99]
    missing = set(range(a + 1, b)) - set(t[86:99])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]