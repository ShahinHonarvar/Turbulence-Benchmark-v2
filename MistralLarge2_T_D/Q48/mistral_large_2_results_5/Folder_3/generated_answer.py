def return_binary_or_hexa(num_tuple):
    a = num_tuple[56]
    b = num_tuple[88]
    sub_tuple = num_tuple[56:89]
    missing_nums = [x for x in range(a + 1, b) if x not in sub_tuple]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]