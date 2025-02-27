def return_binary_or_hexa(nums):
    a = nums[72]
    b = nums[93]
    if a + 1 >= b:
        return ''
    present = set(nums[72:94])
    sum_missing = sum((x for x in range(a + 1, b) if x not in present))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]