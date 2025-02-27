def return_binary_or_hexa(tup):
    a, b = (tup[34], tup[69])
    missing_numbers = set(range(a + 1, b)) - set(tup[34:69])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()