def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(4):
        if i % 2 == 1:
            sum += nums[i]
    return sum if sum else 0