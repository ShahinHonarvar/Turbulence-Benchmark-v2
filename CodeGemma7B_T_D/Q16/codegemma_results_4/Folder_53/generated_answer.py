def sum_even_ints_inclusive(nums):
    i = 111
    sum = 0
    while i <= 111:
        if nums[i] % 2 == 0:
            sum += nums[i]
        i += 1
    return sum