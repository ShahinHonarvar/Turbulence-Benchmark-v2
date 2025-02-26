def return_binary_or_hexa(input_tuple):
    a = input_tuple[86]
    b = input_tuple[90]
    missing_nums = [num for num in range(a + 1, b) if num not in input_tuple[86:91]]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]