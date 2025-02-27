def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    sum_missing = 0
    for i in range(a + 1, b):
        if i not in nums[30:201]:
            sum_missing += i
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]