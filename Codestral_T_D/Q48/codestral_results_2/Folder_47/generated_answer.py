def return_binary_or_hexa(t):
    a, b = (t[29], t[53])
    s = sum((i for i in range(a + 1, b) if i not in t[29:54]))
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:].lstrip('0') if s != 0 else ''