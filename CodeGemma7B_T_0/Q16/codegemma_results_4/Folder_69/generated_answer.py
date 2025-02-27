def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 32 or len(nums) < 35:
        return 0
    sum = 0
    for i in range(32, 36):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum