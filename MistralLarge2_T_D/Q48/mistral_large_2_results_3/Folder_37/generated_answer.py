def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[7])
    range_nums = set(range(a + 1, b))
    missing_nums = range_nums - set(nums[2:8])
    sum_missing = sum(missing_nums)
    if not missing_nums:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()