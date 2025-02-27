def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    missing = set(range(a + 1, b)) - set(t[57:84])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:].lstrip('0')