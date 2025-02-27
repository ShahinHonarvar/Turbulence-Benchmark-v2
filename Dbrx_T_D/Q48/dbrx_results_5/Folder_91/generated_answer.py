def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[0], int_tuple[6])
    present_set = set(int_tuple[1:7])
    missing_set = set(range(a + 1, b))
    missing_set.difference_update(present_set)
    if not missing_set:
        return ''
    sum_val = sum(missing_set)
    if sum_val % 2:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)