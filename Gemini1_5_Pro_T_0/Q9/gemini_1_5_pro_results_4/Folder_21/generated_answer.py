def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(max(0, 639), min(len(nums), 976)):
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds