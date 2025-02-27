def return_binary_or_hexa(tup):
    a = tup[275]
    b = tup[871]
    missing_numbers = set(range(a + 1, b)) - set(tup[275:872])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
    return ''