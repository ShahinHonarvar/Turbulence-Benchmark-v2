def return_binary_or_hexa(t):
    a, b = (t[90], t[200])
    s = sum(set(range(a + 1, b)) - set(t[91:200]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]