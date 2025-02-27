def return_binary_or_hexa(nums):
    a = nums[17]
    b = nums[88]
    present_numbers = set(nums[17:89])
    sum_missing = sum((x for x in range(a + 1, b) if x not in present_numbers))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]