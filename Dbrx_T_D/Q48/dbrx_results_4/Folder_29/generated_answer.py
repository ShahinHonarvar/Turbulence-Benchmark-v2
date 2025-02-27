def return_binary_or_hexa(int_tuple):
    a = int_tuple[70]
    b = int_tuple[98]
    sum_of_missing = sum(set(range(a + 1, b)) - set(int_tuple[70:99]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()