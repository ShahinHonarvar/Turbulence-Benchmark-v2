def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    s = set(list(range(a + 1, b)))
    not_in_t = s.difference(t[18:89])
    Rs = sum(not_in_t)
    if Rs % 2 == 0:
        return format(Rs, 'x')
    else:
        return format(Rs, 'b')