def sum_odd_ints_inclusive(nums):
    return sum((x for x in nums[0:9] if x % 2 != 0))