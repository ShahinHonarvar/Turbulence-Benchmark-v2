def return_binary_or_hexa(nums):
    if len(nums) <= 5:
        return ''
    a = nums[2]
    b = nums[5]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in nums[2:6]))
    if sum_of_missing == 0:
        return ''
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]