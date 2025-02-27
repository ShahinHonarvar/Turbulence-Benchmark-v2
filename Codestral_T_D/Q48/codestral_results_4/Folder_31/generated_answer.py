def return_binary_or_hexa(nums):
    a = nums[33]
    b = nums[78]
    missing_nums = set(range(a + 1, b)) - set(nums[33 + 1:78])
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]