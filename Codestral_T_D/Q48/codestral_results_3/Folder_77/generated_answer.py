def return_binary_or_hexa(tup):
    a, b = (tup[18], tup[52])
    missing = set(range(a + 1, b)) - set(tup[18 + 1:52])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''