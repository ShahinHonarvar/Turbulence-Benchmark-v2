def return_binary_or_hexa(t):
    a, b = (t[20], t[43])
    s = sum(set(range(a + 1, b)) - set(t[20:44]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]