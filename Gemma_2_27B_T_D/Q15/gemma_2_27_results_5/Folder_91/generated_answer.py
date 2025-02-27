def sum_odd_ints_inclusive(nums):
    sum_of_odds = 0
    for i in range(6):
        if i < len(nums) and nums[i] % 2 != 0:
            sum_of_odds += nums[i]
    return sum_of_odds