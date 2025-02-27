def return_binary_or_hexa(tup):
    a, b = (tup[36], tup[54])
    sum_missing = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_missing += i
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()