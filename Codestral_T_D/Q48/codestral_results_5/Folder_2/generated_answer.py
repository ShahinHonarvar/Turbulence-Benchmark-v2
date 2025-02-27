def return_binary_or_hexa(nums):
    a = nums[72]
    b = nums[93]
    missing = set(range(a + 1, b)) - set(nums[72 + 1:93])
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''