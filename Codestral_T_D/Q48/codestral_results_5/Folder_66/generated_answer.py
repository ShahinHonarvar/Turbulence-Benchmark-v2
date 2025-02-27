def return_binary_or_hexa(tup):
    a, b = (tup[11], tup[76])
    s = sum((i for i in range(a + 1, b) if i not in tup[11:77]))
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]