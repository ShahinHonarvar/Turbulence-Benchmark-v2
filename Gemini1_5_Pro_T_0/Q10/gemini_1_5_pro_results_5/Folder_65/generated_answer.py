def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(42, 87):
        if i < len(nums) and nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds