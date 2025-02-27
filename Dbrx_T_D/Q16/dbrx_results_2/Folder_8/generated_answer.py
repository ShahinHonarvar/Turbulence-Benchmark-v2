def sum_even_ints_inclusive(nums):
    if len(nums) < 23:
        return 0
    start_index = 23 - 1
    end_index = min(len(nums) - 1, 23)
    sum = 0
    for i in range(start_index, end_index + 1):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum