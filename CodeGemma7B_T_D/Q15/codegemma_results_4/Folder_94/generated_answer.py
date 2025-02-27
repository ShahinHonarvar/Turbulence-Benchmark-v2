def sum_odd_ints_inclusive(nums):
    res = 0
    for i in range(28, 42):
        if i not in nums:
            continue
        if i % 2:
            res += nums[i]
    return res