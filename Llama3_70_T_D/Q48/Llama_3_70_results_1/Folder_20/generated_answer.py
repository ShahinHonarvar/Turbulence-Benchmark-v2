def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]
    missing_nums = set(range(a + 1, b)) - set(nums[27:97])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]