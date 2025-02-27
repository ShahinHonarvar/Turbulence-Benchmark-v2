def return_binary_or_hexa(tup):
    a = tup[49]
    b = tup[74]
    total = 0
    for i in range(a + 1, b):
        if i not in tup:
            total += i
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]