def return_binary_or_hexa(t):
    a = t[0]
    b = t[5]
    missing = set(range(a + 1, b)) - set(t[1:6])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]