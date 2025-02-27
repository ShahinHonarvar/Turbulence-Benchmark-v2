def return_binary_or_hexa(t):
    a = t[42]
    b = t[87]
    s = sum((x for x in range(a + 1, b) if x not in t[42:87]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]