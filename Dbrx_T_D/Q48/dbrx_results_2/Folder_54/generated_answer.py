def return_binary_or_hexa(int_tuple):
    a = int_tuple[35]
    b = int_tuple[64]
    present_set = set(int_tuple[36:64])
    missing_set = set(range(a + 1, b)) - present_set
    if not missing_set:
        return ''
    sum_val = sum(missing_set)
    if sum_val % 2:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()