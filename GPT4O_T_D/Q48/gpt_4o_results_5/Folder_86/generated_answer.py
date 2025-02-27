def return_binary_or_hexa(nums):
    if len(nums) < 33:
        return ''
    a, b = (nums[19], nums[32])
    sum_missing = sum((i for i in range(a + 1, b) if i not in nums[20:32]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]