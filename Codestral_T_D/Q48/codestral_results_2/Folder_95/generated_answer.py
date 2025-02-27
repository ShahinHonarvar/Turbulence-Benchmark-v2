def return_binary_or_hexa(nums):
    a, b = (nums[32], nums[99])
    missing_nums = set(range(a + 1, b)) - set(nums[32:100])
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]