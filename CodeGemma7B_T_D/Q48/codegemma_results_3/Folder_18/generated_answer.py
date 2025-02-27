def return_binary_or_hexa(tup):
    a = tup[56]
    b = tup[90]
    sum_missing = 0
    for i in range(a + 1, b):
        if i not in tup[56:91]:
            sum_missing += i
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    return bin(sum_missing)[2:]