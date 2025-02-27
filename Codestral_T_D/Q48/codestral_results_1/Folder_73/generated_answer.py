def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[76]
    missing_numbers = [i for i in range(a + 1, b) if i not in tup[10:76]]
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]