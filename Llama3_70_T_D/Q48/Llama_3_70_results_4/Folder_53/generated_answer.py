def return_binary_or_hexa(nums):
    a, _, b = nums[200:203]
    missing_nums = set(range(a + 1, b)) - set(nums[200:203])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]