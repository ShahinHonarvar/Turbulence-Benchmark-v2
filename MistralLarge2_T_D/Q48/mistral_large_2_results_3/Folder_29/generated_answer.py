def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[98]
    sum_missing = 0
    for i in range(a + 1, b):
        if i not in nums[70:99]:
            sum_missing += i
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()