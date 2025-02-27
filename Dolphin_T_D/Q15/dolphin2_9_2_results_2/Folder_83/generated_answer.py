def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums[90:201]) if i % 2 != 0))