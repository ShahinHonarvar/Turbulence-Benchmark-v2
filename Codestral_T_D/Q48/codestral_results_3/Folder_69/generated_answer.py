def return_binary_or_hexa(tup):
    a = tup[39]
    b = tup[43]
    missing = set(range(a + 1, b)) - set(tup[39:44])
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]