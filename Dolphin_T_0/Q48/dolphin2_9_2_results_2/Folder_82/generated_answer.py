def return_binary_or_hexa(t):
    a, b = (t[20], t[200])
    if all((i in t for i in range(a + 1, b))):
        return ''
    s = sum(set(range(a + 1, b + 1)) - set(t[21:200]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]