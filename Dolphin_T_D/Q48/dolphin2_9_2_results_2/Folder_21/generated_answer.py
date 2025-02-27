def return_binary_or_hexa(t):
    a, b = (t[15], t[57])
    s = sum((x for x in range(a + 1, b) if x not in t[16:57]))
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:].upper() if s != 0 else ''