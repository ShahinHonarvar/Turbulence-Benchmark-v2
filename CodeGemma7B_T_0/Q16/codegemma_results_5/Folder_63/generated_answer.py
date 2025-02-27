def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(22, 89):
        if i % 2 == 0:
            sum += nums[i]
    if sum == 0:
        return 0
    else:
        return sum