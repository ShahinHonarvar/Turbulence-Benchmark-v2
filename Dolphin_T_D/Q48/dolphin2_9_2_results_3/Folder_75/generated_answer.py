def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[51]
    for i in range(a + 1, b):
        if i not in tup[20:52]:
            return bin(i)[2:] if sum(tup[21:50]) % 2 == 1 else hex(i)[2:]
    return ''