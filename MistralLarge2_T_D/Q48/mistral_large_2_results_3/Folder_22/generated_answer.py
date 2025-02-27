def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    num_set = set(nums[40:201])
    sum_missing = sum((i for i in range(a + 1, b) if i not in num_set))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()