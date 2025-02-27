def return_binary_or_hexa(nums):
    a = nums[25]
    b = nums[80]
    nums_set = set(nums[25:81])
    sum_missing = sum((x for x in range(a + 1, b) if x not in nums_set))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]