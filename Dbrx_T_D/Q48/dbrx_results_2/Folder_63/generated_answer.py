def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[81], int_tuple[86])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in int_tuple[81:87]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()