def return_binary_or_hexa(tup):
    a, b = (tup[86], tup[89])
    sum_of_missing = 0
    for i in range(a + 1, b):
        if i not in tup[86:90]:
            sum_of_missing += i
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()