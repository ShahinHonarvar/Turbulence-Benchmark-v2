def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(66, 94):
        if i in range(len(nums)) and nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds