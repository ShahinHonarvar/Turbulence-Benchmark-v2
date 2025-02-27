def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(max(0, min(91, len(nums))), min(100, len(nums))):
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds