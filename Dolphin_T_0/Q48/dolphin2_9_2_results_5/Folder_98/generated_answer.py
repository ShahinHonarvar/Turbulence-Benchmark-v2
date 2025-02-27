def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    if set(range(a + 1, b)) - set(t[7:]) == set(range(a + 1, b)):
        return ''
    s = sum(set(range(a + 1, b)) - set(t[7:]))
    if s % 2 == 0:
        return hex(s).replace('0x', '')
    else:
        return bin(s)[2:]