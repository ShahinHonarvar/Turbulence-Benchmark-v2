def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[91]
    range_set = set(tup[44:92])
    sum_missing = sum((num for num in range(a + 1, b) if num not in range_set))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]