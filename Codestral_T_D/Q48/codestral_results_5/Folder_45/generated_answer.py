def return_binary_or_hexa(tup):
    a = tup[30]
    b = tup[200]
    s = sum((i for i in range(a + 1, b) if i not in tup[30:200]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]