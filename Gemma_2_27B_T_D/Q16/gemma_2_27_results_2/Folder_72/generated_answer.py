def sum_even_ints_inclusive(nums):
    return sum(nums[29:52:1]) if len([x for x in nums[29:52:1] if x % 2 == 0]) > 0 else 0