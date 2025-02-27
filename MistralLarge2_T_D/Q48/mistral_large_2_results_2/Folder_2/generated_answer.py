def return_binary_or_hexa(nums):
    a = nums[72]
    b = nums[93]
    sum_missing = 0
    present_nums = set(nums[72:94])
    for num in range(a + 1, b):
        if num not in present_nums:
            sum_missing += num
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()