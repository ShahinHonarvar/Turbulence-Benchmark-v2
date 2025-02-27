def return_binary_or_hexa(tup):
    a, b = (tup[56], tup[88])
    missing_numbers = set(range(a + 1, b)) - set(tup[56:89])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()