def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(max(0, min(55, len(nums) - 1)), min(98, len(nums) - 1) + 1):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum