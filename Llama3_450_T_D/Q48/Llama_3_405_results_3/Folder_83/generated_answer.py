def return_binary_or_hexa(nums):
    a = nums[90]
    b = nums[200]
    missing_nums = set(range(a + 1, b)) - set(nums[91:200])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]