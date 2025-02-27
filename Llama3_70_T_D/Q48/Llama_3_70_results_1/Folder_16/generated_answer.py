def return_binary_or_hexa(tup):
    a = tup[90]
    b = tup[97]
    s = sum((i for i in range(a + 1, b) if i not in tup[90:97]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]