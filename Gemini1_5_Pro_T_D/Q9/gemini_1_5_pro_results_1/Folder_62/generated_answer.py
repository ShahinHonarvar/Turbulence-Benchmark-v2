def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(91, 100):
        if i >= len(nums):
            break
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds