def return_binary_or_hexa(tup):
    a = tup[11]
    b = tup[76]
    total = sum((i for i in range(a + 1, b) if i not in tup[11:77]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]