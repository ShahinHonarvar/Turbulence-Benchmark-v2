def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(40, 81):
        if nums[i] % 2 != 0:
            total += nums[i]
    return total if total != 0 else 0