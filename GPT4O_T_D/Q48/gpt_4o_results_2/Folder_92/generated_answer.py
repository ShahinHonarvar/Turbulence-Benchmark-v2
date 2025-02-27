def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[2]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in nums[1:3]))
    if sum_of_missing == 0:
        return ''
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]