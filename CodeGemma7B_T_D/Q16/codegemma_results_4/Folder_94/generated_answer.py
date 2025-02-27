def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(28, 41):
        if i % 2 == 0:
            sum += nums[i]
    return sum if sum else 0