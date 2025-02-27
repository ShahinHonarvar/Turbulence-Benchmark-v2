def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[79])
    subset = set(nums[10:80])
    sum_missing = sum((x for x in range(a + 1, b) if x not in subset))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]