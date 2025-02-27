def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 25 or len(nums) < 59:
        return 0
    sum = 0
    for i in range(25, 60):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum