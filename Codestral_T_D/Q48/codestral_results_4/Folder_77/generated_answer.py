def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[52]
    missing_nums = set(range(a + 1, b)) - set(nums[18:53])
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''