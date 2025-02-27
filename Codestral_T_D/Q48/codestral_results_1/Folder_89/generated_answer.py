def return_binary_or_hexa(tup):
    a, b = (tup[55], tup[84])
    missing = set(range(a + 1, b)) - set(tup[55 + 1:84])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''