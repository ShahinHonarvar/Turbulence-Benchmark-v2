def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(max(0, min(len(nums) - 1, 59) + 1), max(0, min(len(nums), 93) - 1)):
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds