def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[9]
    missing_nums = set(range(a + 1, b)) - set(nums[3:10])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]