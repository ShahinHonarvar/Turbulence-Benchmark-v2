def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(4, len(nums) - 2, 2):
        if nums[i] % 2 == 1:
            odds.append(nums[i])
    return odds