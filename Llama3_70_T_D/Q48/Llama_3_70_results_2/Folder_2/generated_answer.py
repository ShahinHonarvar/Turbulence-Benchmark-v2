def return_binary_or_hexa(tup):
    a = tup[72]
    b = tup[93]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in tup[72:94]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]