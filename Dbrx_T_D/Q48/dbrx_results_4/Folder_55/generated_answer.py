def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[10], int_tuple[12])
    sum_of_missing = sum(set(range(a + 1, b)) - set(int_tuple[10:13]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()