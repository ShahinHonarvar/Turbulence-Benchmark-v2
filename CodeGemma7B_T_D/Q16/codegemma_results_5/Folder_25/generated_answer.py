def sum_even_ints_inclusive(nums):
    if not nums or index(nums, 29) == -1 or index(nums, 93) == -1:
        return 0
    sum = 0
    for i in range(index(nums, 29), index(nums, 93) + 1):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum