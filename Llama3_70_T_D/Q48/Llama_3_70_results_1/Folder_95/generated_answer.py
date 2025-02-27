def return_binary_or_hexa(nums):
    a, b = (nums[32], nums[99])
    total = sum((i for i in range(a + 1, b) if i not in nums[32:100]))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]