def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[8]
    missing = set(range(a + 1, b)) - set(nums[3:9])
    sum_missing = sum(missing)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]