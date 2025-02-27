def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    all_nums = set(range(a + 1, b))
    present_nums = set(nums[61:91])
    missing_nums = all_nums - present_nums
    if not missing_nums:
        return ''
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]