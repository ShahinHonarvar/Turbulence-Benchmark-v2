def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[28])
    subset = set(nums[10:29])
    total = sum((x for x in range(a + 1, b) if x not in subset))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]