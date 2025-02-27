def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 42 or len(nums) < 68:
        return 0
    sum = 0
    for i in range(42, 69):
        if i < len(nums) and nums[i] % 2 == 0:
            sum += nums[i]
    return sum