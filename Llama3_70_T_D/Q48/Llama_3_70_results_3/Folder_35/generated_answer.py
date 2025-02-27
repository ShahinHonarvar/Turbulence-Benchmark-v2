def return_binary_or_hexa(tup):
    a = tup[77]
    b = tup[84]
    specified_range = set(tup[77:85])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in specified_range))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]