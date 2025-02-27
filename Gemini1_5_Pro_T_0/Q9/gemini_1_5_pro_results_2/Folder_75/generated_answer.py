def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(max(0, min(len(nums) - 1, 56)), min(len(nums), 58)):
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds