def return_binary_or_hexa(nums):
    a, b = (nums[33], nums[78])
    missing = set(range(a + 1, b)) - set(nums[33:78])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]