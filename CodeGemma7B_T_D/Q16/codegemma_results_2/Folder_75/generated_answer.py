def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(56, 58 + 1):
        if i >= 0 and i < len(nums) and (nums[i] % 2 == 0):
            result += nums[i]
    return result if result != 0 else 0