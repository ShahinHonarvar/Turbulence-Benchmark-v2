def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[6])
    missing_numbers = set(range(a + 1, b)) - set(tup[:7])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    return hex(sum_missing)[2:]