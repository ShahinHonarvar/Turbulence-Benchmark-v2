def return_binary_or_hexa(tup):
    a = tup[16]
    b = tup[87]
    total = sum((i for i in range(a + 1, b) if i not in tup[16:88]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]