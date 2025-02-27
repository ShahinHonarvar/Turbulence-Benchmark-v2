def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[90]
    sum_missing = 0
    present_set = set(nums[86:91])
    for num in range(a + 1, b):
        if num not in present_set:
            sum_missing += num
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()