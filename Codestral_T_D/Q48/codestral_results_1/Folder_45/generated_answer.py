def return_binary_or_hexa(t):
    a = t[30]
    b = t[200]
    s = sum((x for x in range(a + 1, b) if x not in t[30:201]))
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:] if s != 0 else ''