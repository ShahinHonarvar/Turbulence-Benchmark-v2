def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(29, 52):
        if i >= 0 and i <= len(nums) - 1 and (nums[i] % 2 == 0):
            total += nums[i]
    if total == 0:
        return 0
    return total