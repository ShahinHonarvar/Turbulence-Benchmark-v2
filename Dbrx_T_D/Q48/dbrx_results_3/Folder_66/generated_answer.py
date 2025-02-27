def return_binary_or_hexa(nums):
    a, b = (nums[11], nums[76])
    all_nums = set(range(a + 1, b))
    present_nums = set(nums[12:77])
    missing_nums = all_nums - present_nums
    if not missing_nums:
        return ''
    sum_of_missing = sum(missing_nums)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()