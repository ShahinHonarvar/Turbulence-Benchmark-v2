def gcf_three_nums(nums):
    """Calculates the greatest common factor of three numbers at specific indices within a list."""
    return gcd(nums[36], gcd(nums[85], nums[83]))

def gcd(a, b):
    """Computes the greatest common divisor of two numbers."""
    if b == 0:
        return a
    return gcd(b, a % b)