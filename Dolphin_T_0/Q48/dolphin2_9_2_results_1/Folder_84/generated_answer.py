def return_binary_or_hexa(t):
    a, b = (t[32], t[44])
    s = sum(set(range(a + 1, b)) - set(t[33:44]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]