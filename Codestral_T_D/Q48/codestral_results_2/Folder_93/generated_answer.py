def return_binary_or_hexa(tup):
    a, b = (tup[57], tup[85])
    s = sum(set(range(a + 1, b)) - set(tup[57 + 1:85]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]