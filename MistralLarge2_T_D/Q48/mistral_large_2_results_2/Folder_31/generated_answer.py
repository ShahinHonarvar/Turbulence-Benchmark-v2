def return_binary_or_hexa(nums):
    a, b = (nums[33], nums[78])
    present = set(nums[33:79])
    total = sum((x for x in range(a + 1, b) if x not in present))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]