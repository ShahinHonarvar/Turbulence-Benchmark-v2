def return_binary_or_hexa(nums):
    a, b = (nums[81], nums[86])
    sum_missing = sum(set(range(a + 1, b)) - set(nums[81:87]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]