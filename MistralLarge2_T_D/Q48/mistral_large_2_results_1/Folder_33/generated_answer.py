def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[35]
    sum_missing = sum(set(range(a + 1, b)) - set(nums[13:36]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]