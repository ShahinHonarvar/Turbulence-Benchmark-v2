def return_binary_or_hexa(int_tuple):
    a = int_tuple[72]
    b = int_tuple[93]
    sum_not_in_range = sum((i for i in range(a + 1, b) if i not in int_tuple[72:93]))
    if sum_not_in_range % 2:
        return bin(sum_not_in_range)[2:]
    else:
        return hex(sum_not_in_range)[2:].upper()