def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(533, 606):
        if i >= 0 and i <= len(nums) - 1 and (nums[i] % 2 == 0):
            result += nums[i]
    if result == 0:
        return 0
    else:
        return result