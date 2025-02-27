def return_binary_or_hexa(t):
    a, _, b = t
    s = sum(set(range(a + 1, b)) - set(t[1:]))
    return bin(s)[2:] if s % 2 == 1 else hex(s)[2:]