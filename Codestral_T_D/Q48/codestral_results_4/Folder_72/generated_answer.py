def return_binary_or_hexa(t):
    a, b = (t[13], t[70])
    missing = set(range(a + 1, b)) - set(t[13 + 1:70])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]