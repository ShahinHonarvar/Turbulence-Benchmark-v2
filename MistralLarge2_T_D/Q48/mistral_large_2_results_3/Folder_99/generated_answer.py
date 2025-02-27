def return_binary_or_hexa(tup):
    a = tup[427]
    b = tup[669]
    s = sum(set(range(a + 1, b)) - set(tup[427:670]))
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]