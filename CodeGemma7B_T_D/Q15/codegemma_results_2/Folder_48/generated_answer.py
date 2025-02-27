def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(533, 606):
        if i >= 533 and i <= 605 and (nums[i] % 2 != 0):
            sum += nums[i]
    return sum