def return_binary_or_hexa(tuple_nums):
    a = tuple_nums[110]
    b = tuple_nums[348]
    missing_nums = set(range(a + 1, b))
    for num in tuple_nums[110:349]:
        if num in missing_nums:
            missing_nums.remove(num)
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]