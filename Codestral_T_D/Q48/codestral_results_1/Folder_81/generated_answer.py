def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[100]
    missing_nums = set(range(a + 1, b)) - set(nums[10:101])
    total = sum(missing_nums)
    if total % 2 != 0:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''