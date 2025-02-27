def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    nums_range = set(nums[29:54])
    total = sum((i for i in range(a + 1, b) if i not in nums_range))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]