def sum_even_ints_inclusive(nums):
    start = 82
    end = 86
    sum_even = 0
    for i in range(start, end + 1):
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    return sum_even