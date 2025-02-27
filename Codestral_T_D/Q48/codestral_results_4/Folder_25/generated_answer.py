def return_binary_or_hexa(nums):
    a, b = (nums[37], nums[43])
    missing_nums = set(range(a + 1, b)) - set(nums[37 + 1:43])
    if not missing_nums:
        return ''
    else:
        sum_missing = sum(missing_nums)
        if sum_missing % 2 != 0:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]