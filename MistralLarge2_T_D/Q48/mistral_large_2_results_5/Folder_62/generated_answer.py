def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[92]
    sum_missing = sum((x for x in range(a + 1, b) if x not in nums[50:93]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]