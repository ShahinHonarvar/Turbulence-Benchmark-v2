def sum_in_range(nums):
    return sum((num for num in nums if num in range(-3, 7))) or 0