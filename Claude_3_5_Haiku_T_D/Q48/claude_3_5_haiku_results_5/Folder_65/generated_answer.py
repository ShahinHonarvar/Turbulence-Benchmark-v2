def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[51]
    b = sorted_tuple[76]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in sorted_tuple[51:77]:
            missing_nums.append(num)
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]