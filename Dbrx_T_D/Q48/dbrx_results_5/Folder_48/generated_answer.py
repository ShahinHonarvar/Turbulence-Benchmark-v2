def return_binary_or_hexa(nums):
    a, b = (nums[933], nums[996])
    if a + 1 > b - 1:
        return ''
    missing_nums = set(range(a + 1, b))
    present_nums = set(nums[933:997])
    missing_nums -= present_nums
    sum_missing = sum(missing_nums)
    if sum_missing % 2:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x').upper()