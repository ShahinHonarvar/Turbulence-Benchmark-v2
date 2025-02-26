def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[29]
    b = nums_tuple[53]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in nums_tuple[29:54]:
            missing_nums.append(num)
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]