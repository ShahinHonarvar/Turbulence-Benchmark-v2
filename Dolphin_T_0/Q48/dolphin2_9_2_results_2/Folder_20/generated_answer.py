def return_binary_or_hexa(num_tuple):
    a = num_tuple[27]
    b = num_tuple[96]
    range_num = set(range(a + 1, b))
    tuple_num = set(num_tuple[27:97])
    missing_num = list(range_num - tuple_num)
    if not missing_num:
        return ''
    sum_missing = sum(missing_num)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]