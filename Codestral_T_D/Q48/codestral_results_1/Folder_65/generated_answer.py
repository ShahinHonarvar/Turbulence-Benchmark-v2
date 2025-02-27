def return_binary_or_hexa(nums):
    a = nums[51]
    b = nums[76]
    range_nums = set(nums[51 + 1:76])
    missing_nums = set(range(a + 1, b)) - range_nums
    if not missing_nums:
        return ''
    else:
        sum_missing = sum(missing_nums)
        if sum_missing % 2 == 1:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]