def sum_odd_ints_inclusive(nums):
    if nums:
        return sum((x for x in nums[0:1] if x % 2 != 0)) + sum((x for x in nums if x % 2 != 0 and nums.index(x) != 0))
    else:
        return 0