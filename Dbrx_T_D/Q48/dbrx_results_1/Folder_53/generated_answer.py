def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    if a + 1 >= b:
        return ''
    missing_nums = set(range(a + 1, b))
    missing_nums -= set(nums[200:203])
    if not missing_nums:
        return ''
    sum_of_missing = sum(missing_nums)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()