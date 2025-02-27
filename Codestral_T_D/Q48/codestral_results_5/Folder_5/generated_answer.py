def return_binary_or_hexa(t):
    a, b = (t[2], t[8])
    missing = set(range(a + 1, b)) - set(t[2:8])
    s = sum(missing)
    if s:
        return bin(s)[2:] if s % 2 else hex(s)[2:]
    else:
        return ''