def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[35]
    sum_missing = sum((i for i in range(a + 1, b) if i not in nums[14:36]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    return hex(sum_missing)[2:]