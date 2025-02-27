def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(70, 201):
        if i % 2 == 1 and i in nums:
            sum_odd += nums[i]
    return sum_odd