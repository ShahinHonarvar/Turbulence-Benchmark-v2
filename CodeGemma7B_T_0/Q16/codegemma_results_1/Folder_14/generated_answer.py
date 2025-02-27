def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 5 or len(nums) < 8:
        return 0
    sum = 0
    for i in range(5, 8 + 1):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum