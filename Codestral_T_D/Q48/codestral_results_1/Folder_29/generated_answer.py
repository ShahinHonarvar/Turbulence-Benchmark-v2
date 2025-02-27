def return_binary_or_hexa(tup):
    a = tup[70]
    b = tup[98]
    missing = set(range(a + 1, b)) - set(tup[71:98])
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]