def return_binary_or_hexa(tuple_ints):
    a, b = (tuple_ints[3], tuple_ints[9])
    sum_of_missing = sum(set(range(a + 1, b)) - set(tuple_ints[3:10]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()