def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[89]
    missing_nums = set(range(a + 1, b)) - set(nums[86:90])
    total = sum(missing_nums)
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]