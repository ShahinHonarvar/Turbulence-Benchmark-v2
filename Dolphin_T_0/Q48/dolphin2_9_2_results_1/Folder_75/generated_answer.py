def return_binary_or_hexa(t):
    a, b = (t[20], t[51])
    s = sum(set(range(a + 1, b)) - set(t[21:51]))
    return bin(s)[2:] if s % 2 else hex(s)[2:] if s != '' else ''