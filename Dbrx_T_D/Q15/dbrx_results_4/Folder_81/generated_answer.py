def sum_odd_ints_inclusive(nums):
    return sum((x for x in nums[9:100] if x % 2 != 0))