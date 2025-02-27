def return_binary_or_hexa(tup):
    a, b = (tup[44], tup[78])
    missing = set(range(a + 1, b)) - set(tup[45:78])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''