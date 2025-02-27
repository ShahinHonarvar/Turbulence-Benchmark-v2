def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(max(31, 0), min(len(nums), 73)):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum