def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]
    full_range = set(range(a + 1, b))
    present_nums = set(nums[27:97])
    missing_nums = full_range - present_nums
    total = sum(missing_nums)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]