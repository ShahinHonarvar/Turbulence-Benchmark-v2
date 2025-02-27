def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[5])
    sum_missing = sum((x for x in range(a + 1, b) if x not in nums[2:6]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]