def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    s = sum((x for x in range(a + 1, b) if x not in tup[1:4]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]