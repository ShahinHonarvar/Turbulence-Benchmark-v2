def return_binary_or_hexa(num_tuple):
    a = num_tuple[36]
    b = num_tuple[52]
    present_nums = num_tuple[36:52]
    missing_nums = [x for x in range(a + 1, b) if x not in present_nums]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]