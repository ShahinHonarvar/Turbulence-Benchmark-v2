def return_binary_or_hexa(nums):
    a, b = (nums[18], nums[60])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in nums[18:61]))
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x').upper()