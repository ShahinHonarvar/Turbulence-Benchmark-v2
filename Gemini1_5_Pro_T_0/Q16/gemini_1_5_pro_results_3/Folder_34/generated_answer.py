def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(max(60, 0), min(len(nums), 201)):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum