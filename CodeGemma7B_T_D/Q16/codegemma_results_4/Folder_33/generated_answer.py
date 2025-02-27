def sum_even_ints_inclusive(nums):
    total_sum = 0
    for i in range(667, 775):
        if i >= 667 and i <= 774 and (nums[i] % 2 == 0):
            total_sum += nums[i]
    return total_sum