def return_binary_or_hexa(t):
    a, b = (t[45], t[48])
    s = sum((x for x in range(a + 1, b) if x not in t[45:48]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper() if s else ''