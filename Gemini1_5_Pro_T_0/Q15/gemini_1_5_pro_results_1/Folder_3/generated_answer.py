def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(max(0, min(62, len(nums))), min(93, len(nums))):
        if nums[i] % 2 != 0:
            total += nums[i]
    return total