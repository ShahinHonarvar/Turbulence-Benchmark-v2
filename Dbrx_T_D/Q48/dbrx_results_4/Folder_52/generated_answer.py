def return_binary_or_hexa(int_tuple):
    a = int_tuple[38]
    b = int_tuple[81]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in int_tuple[38:82]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()