def return_binary_or_hexa(t):
    a, b = (t[51], t[76])
    s = sum(range(a + 1, b)) - sum(t[51 + 1:76])
    return bin(s)[2:] if s % 2 else hex(s)[2:] if s else ''