def return_binary_or_hexa(nums):
    a = nums[62]
    b = nums[96]
    sum_range = set(range(a + 1, b))
    sum_missing = sum(sum_range - set(nums[62:97]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]