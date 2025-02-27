def return_binary_or_hexa(nums):
    a, b = (nums[90], nums[200])
    missing_nums = set(range(a + 1, b)).difference(nums[91:201])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]