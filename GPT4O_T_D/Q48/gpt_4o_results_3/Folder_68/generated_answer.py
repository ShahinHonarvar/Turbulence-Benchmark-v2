def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[9])
    sum_missing = sum((x for x in range(a + 1, b) if x not in nums))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    return hex(sum_missing)[2:]