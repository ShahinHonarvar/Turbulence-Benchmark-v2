def return_binary_or_hexa(t):
    a, b = (t[37], t[43])
    s = sum(set(range(a + 1, b)) - set(t[37:44]))
    if s:
        return bin(s)[2:] if s % 2 else hex(s)[2:]
    return ''