def return_binary_or_hexa(nums):
    a = nums[55]
    b = nums[84]
    excluded_range = set(nums[55:85])
    sum_not_present = sum((num for num in range(a + 1, b) if num not in excluded_range))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]