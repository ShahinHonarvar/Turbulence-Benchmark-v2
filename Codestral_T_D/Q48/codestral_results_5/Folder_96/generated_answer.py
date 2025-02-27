def return_binary_or_hexa(tup):
    a = tup[50]
    b = tup[200]
    s = sum((i for i in range(a + 1, b) if i not in tup[50:201]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]