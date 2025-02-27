def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(11, 12):
        if i >= len(nums):
            break
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds