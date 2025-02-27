def sum_even_ints_inclusive(nums):
    count = 0
    sum = 0
    for i in range(52, 72):
        if nums[i] % 2 == 0:
            count += 1
            sum += nums[i]
    return count * sum