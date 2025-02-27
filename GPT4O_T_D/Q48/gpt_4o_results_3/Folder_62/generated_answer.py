def return_binary_or_hexa(nums):
    a, b = (nums[50], nums[92])
    sum_missing = sum((i for i in range(a + 1, b) if i not in nums[51:93]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]