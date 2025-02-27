def return_binary_or_hexa(t):
    a, b = (t[39], t[43])
    missing = set(range(a + 1, b)) - set(t[39 + 1:43])
    s = sum(missing)
    if s:
        return bin(s)[2:] if s % 2 else hex(s)[2:]
    return ''