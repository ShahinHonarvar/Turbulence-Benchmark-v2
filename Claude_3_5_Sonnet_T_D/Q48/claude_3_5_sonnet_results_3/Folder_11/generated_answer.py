def return_binary_or_hexa(nums):
    a = nums[48]
    b = nums[76]
    excluded = set(nums[48:77])
    total = sum((x for x in range(a + 1, b) if x not in excluded))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].rstrip('L')