def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(20, 201):
        if i % 2 != 0:
            sum += nums[i]
    return sum if sum != 0 else 0