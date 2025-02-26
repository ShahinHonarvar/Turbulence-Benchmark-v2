def sum_odd_ints_inclusive(nums):
    if len(nums) < 8:
        return 0
    sum_odds = 0
    for num in nums[5:8]:
        if num % 2 != 0:
            sum_odds += num
    return sum_odds