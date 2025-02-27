def return_binary_or_hexa(tup):
    a = tup[32]
    b = tup[44]
    total = 0
    for i in range(a + 1, b):
        if i not in tup[32:45]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]