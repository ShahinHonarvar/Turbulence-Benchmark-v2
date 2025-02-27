def return_binary_or_hexa(nums):
    a, b = (nums[86], nums[89])
    if a + 1 > b - 1:
        return ''
    missing_nums = set(range(a + 1, b)) - set(nums[86:90])
    sum_missing = sum(missing_nums)
    if sum_missing % 2:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')