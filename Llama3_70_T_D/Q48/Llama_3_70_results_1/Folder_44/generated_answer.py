def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[52]
    s = sum((i for i in range(a + 1, b) if i not in tup[36:53]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]