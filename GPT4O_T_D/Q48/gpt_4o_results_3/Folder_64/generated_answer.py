def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[5]
    nums_in_range = set(nums[:6])
    sum_missing = sum((x for x in range(a + 1, b) if x not in nums_in_range))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]