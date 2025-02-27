def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(90, 202):
        if i >= 90 and i <= 200 and (nums[i] % 2 == 0):
            sum += nums[i]
    return sum or 0