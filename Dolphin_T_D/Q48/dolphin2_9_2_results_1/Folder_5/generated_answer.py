def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[8]
    s = sum(set(range(a + 1, b)) - set(tup[3:8]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]