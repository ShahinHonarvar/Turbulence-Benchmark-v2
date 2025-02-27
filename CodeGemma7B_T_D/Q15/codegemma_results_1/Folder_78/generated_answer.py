def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(43, 52):
        if i in range(43, 52) and nums[i] % 2 == 1:
            total += nums[i]
    return total if total else 0