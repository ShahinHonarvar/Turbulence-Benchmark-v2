def return_binary_or_hexa(nums):
    a, b = (nums[55], nums[84])
    existing_nums = set(nums[55:85])
    sum_missing = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]