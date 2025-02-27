from functools import reduce

def sum_odd_ints_inclusive(nums):
    return reduce(lambda x, y: x + y, [num for num in nums[23:24] if num % 2 != 0], 0)