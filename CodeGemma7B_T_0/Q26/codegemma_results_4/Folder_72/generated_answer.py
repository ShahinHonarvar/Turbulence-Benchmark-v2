def sum_in_range(nums):
    return sum((num for num in nums if num in range(46, 92))) or 0