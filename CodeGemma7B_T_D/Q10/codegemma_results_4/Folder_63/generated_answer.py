def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(38, 52):
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds