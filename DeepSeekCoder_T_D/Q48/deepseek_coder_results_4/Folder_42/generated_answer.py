def return_binary_or_hexa(tup):
    a = tup[18]
    b = tup[60]
    missing_numbers = set(range(a + 1, b)) - set(tup[18:61])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]