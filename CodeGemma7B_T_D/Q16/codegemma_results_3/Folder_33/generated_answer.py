def sum_even_ints_inclusive(nums):
    i = 667
    sum = 0
    while i <= 774:
        if i % 2 == 0:
            sum += nums[i]
        i += 1
    return sum