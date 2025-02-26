def return_binary_or_hexa(input_tuple):
    a = input_tuple[69]
    b = input_tuple[97]
    set_range = set(input_tuple[69:98])
    sum_missing = sum((x for x in range(a + 1, b) if x not in set_range))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]