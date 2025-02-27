def return_binary_or_hexa(nums):
    a = nums[6] if len(nums) > 6 else 0
    b = nums[9] if len(nums) > 9 else max(nums[6:]) if len(nums) > 6 else 0
    sum_of_missing = sum((x for x in range(a + 1, b) if x not in nums[6:9]))
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x')