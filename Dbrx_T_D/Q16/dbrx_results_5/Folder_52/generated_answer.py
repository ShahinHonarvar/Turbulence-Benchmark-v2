def sum_even_ints_inclusive(nums):
    if len(nums) < 39:
        return 'Input list should have at least 39 elements'
    sum = 0
    for i in range(28, 39):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum