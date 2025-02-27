def return_binary_or_hexa(t):
    a = t[81]
    b = t[86]
    s = sum(set(range(a + 1, b)) - set(t[82:86]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]