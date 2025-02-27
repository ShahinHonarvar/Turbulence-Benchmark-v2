def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[200]
    missing = set(range(a + 1, b)) - set(nums[60:201])
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''