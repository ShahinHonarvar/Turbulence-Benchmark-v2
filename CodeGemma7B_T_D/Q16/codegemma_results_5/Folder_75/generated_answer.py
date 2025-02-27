def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(56, 58):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum if sum else 0