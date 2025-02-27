def sum_odd_ints_inclusive(nums):
    sum_odds = 0
    for i in range(37, 52):
        if i >= 37 and i <= 51 and (nums[i] % 2 != 0):
            sum_odds += nums[i]
    return sum_odds or 0