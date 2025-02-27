def sum_odd_ints_inclusive(nums):
    return sum((nums[75:89] if i % 2 else 0 for i in nums))