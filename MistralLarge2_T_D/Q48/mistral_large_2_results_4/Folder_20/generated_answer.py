def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]
    missing_nums = set(range(a + 1, b)) - set(nums[27:97])
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]