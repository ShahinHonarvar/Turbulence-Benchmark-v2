def return_binary_or_hexa(nums):
    a, b = (nums[29], nums[53])
    num_set = set(nums[29:54])
    sum_missing = sum((x for x in range(a + 1, b) if x not in num_set))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()