def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[35]
    m = set(range(a + 1, b))
    m = m - set(tup[14:35])
    s = sum(m)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]