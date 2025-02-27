def return_binary_or_hexa(nums):
    a, b = (nums[60], nums[90])
    sum_of_missing = sum((x for x in range(a + 1, b) if x not in nums[60:91]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]