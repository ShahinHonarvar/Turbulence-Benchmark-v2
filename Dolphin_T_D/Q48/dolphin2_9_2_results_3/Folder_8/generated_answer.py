def return_binary_or_hexa(t):
    a, b = (t[45], t[48])
    s = sum(set(range(a + 1, b)) - set(t[46:48]))
    return bin(s)[2:] if s % 2 else hex(s)[2:] if s else ''