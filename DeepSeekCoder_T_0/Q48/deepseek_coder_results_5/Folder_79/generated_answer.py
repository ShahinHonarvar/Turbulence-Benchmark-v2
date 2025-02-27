def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[7]
    missing_numbers = set(range(a + 1, b)) - set(tup[1:8])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]