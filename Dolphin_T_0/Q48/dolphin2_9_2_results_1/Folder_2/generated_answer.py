def return_binary_or_hexa(tup):
    a = tup[72]
    b = tup[93]
    s = sum(set(range(a + 1, b)) - set(tup[72:94]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]