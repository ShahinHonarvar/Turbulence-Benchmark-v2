def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(75, 86):
        if i >= len(nums):
            break
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds