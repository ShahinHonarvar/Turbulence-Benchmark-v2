def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(len(nums)):
        if i <= 3:
            if nums[i] % 2 != 0:
                total += nums[i]
    return total if total != 0 else None