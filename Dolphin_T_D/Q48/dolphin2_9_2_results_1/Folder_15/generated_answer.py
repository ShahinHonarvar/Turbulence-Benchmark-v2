def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    s = sum(set(range(a + 1, b)) - set(t[1:5]))
    return bin(s)[2:] if s % 2 else hex(s)[2:] if s != 0 else ''