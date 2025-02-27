def return_binary_or_hexa(nums):
    a, b = (nums[86], nums[89])
    missing_nums = set(range(a + 1, b)) - set(nums[86:89])
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''