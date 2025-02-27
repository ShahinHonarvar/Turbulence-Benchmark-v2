def sum_odd_ints_inclusive(nums):
    sum_odds_within_range = 0
    for num in nums[62:79]:
        if num % 2 == 1:
            sum_odds_within_range += num
    if sum_odds_within_range == 0:
        return 0
    return sum_odds_within_range