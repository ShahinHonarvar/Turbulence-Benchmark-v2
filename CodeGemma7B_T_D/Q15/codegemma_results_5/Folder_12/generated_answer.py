def sum_odd_ints_inclusive(nums):
    res = 0
    for num in nums[14:65]:
        if num % 2 != 0:
            res += num
    return res if res else 0