def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(max(0, min(len(nums), 639)), max(0, min(len(nums), 976))):
        if nums[i] % 2 != 0:
            total += nums[i]
    return total