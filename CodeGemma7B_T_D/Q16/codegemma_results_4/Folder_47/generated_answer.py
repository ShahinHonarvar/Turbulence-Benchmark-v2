def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(37, 77, 2):
        if i >= 0 and i < len(nums):
            if nums[i] % 2 == 0:
                result += nums[i]
    return result