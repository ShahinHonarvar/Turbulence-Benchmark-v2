def gcf_three_nums(nums):
    """Write a function called 'gcf_three_nums' that takes one argument, a list of positive integers, and returns the greatest common factor of the elements at indices 19, 94 and 78."""
    return math.gcd(nums[19], math.gcd(nums[94], nums[78]))