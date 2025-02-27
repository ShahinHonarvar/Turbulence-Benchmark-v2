def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[76]
    sum_missing = sum((x for x in range(a + 1, b) if x not in nums[11:76]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return format(sum_missing, 'x')
    else:
        return format(sum_missing, 'b')