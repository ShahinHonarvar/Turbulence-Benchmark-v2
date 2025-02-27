def sum_even_ints_inclusive(nums):
    total_sum = 0
    for i in range(6, len(nums) + 1):
        if i >= 6 and i <= len(nums) and (nums[i - 1] % 2 == 0):
            total_sum += nums[i - 1]
    if total_sum == 0:
        return 0
    else:
        return total_sum