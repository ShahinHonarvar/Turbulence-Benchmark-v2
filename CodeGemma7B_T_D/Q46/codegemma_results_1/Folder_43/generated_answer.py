import math

def gcf_three_nums(nums):
    num_one, num_two, num_three = (nums[33], nums[78], nums[93])
    return greatest_common_factor(num_one, num_two, num_three)

def greatest_common_factor(*numbers):
    """Finds the greatest common factor of multiple numbers using the Euclidean algorithm."""
    return math.gcd(*numbers)