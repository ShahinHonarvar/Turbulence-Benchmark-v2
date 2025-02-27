def gcf_three_nums(nums):
    """Computes the greatest common factor of the elements at indices 1, 6 and 8."""
    return gcd(gcd(nums[1], nums[6]), nums[8])