def return_binary_or_hexa(nums):
    a, b = (nums[40], nums[200])
    range_set = set(nums[40:201])
    sum_missing = sum((x for x in range(a + 1, b) if x not in range_set))
    if not sum_missing:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]