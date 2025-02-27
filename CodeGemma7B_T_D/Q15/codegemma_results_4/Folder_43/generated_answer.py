def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(68, 87):
        if nums[i] % 2 != 0:
            total += nums[i]
    return total if total else 0