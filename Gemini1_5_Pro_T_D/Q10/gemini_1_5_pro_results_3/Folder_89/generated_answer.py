def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(51, 76):
        if i >= len(nums) or i < 0:
            break
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds