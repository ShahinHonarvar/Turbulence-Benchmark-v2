def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[2])
    s = sum((i for i in range(a + 1, b) if i not in tup[1:2]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]