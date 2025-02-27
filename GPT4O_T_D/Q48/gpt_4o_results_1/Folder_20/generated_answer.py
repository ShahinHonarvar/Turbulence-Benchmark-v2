def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]
    present_nums = set(nums[28:96])
    total = sum((x for x in range(a + 1, b) if x not in present_nums))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]