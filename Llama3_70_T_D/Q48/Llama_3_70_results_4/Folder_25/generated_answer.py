def return_binary_or_hexa(nums):
    a, b = (nums[37], nums[43])
    total = sum((i for i in range(a + 1, b) if i not in nums[37:44]))
    if not total:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]