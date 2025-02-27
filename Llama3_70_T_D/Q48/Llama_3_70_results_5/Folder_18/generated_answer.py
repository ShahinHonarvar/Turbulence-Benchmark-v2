def return_binary_or_hexa(nums):
    a, b = (nums[56], nums[90])
    total = sum((i for i in range(a + 1, b) if i not in nums[57:90]))
    if not total:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]