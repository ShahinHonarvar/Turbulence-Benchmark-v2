def return_binary_or_hexa(t):
    a, b = (t[13], t[35])
    nums_to_check = set(range(a + 1, b))
    present_nums = set(t[13:36])
    missing_nums = nums_to_check - present_nums
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]