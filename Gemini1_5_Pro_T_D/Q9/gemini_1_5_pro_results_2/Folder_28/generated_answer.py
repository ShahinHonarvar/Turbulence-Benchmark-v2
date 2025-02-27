def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(max(0, min(62, len(nums) - 1)), min(63, len(nums) - 1) + 1):
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds