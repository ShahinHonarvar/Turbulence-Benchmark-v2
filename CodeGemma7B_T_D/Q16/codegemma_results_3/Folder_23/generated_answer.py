def sum_even_ints_inclusive(nums):
    if not nums or 52 > len(nums) or 71 > len(nums):
        return 0
    res = 0
    for i in range(52, 72):
        if nums[i] % 2 == 0:
            res += nums[i]
    return res