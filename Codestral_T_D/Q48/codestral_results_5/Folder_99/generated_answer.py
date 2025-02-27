def return_binary_or_hexa(t):
    a, b = (t[427], t[669])
    s = sum(set(range(a + 1, b)) - set(t[427 + 1:669]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]