def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    num_set = set(nums[10:98])
    sum_missing = sum((x for x in range(a + 1, b) if x not in num_set))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]