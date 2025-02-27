def sum_odd_ints_inclusive(nums):
    sum_of_odds = 0
    for i in range(66, 94):
        if i % 2 != 0:
            sum_of_odds += nums[i]
    return sum_of_odds or 0