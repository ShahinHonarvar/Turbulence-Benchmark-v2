def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[8])
    missing_numbers = set(range(a + 1, b)) - set(tup[:9])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]