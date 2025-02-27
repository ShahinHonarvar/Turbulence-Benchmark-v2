def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[81]
    present_set = set(nums[38:82])
    total = sum((x for x in range(a + 1, b) if x not in present_set))
    if total == 0:
        return ''
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]