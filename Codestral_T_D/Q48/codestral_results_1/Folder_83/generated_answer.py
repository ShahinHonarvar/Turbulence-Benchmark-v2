def return_binary_or_hexa(tup):
    a, b = (tup[90], tup[200])
    s = sum(set(range(a + 1, b)) - set(tup[90 + 1:200]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]