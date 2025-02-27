def sum_odd_ints_inclusive(nums):
    sum_odds = 0
    for i in range(62, 79):
        if i >= 62 and i <= 78 and (nums[i] % 2 != 0):
            sum_odds += nums[i]
    if sum_odds == 0:
        return 0
    return sum_odds