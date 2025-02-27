def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(30, 49):
        if i < len(nums) and nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds