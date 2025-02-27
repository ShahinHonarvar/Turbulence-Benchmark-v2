def sum_in_range(nums):
    res = 0
    for num in nums:
        if num in range(350, 470):
            res += num
    return res