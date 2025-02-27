def gcf_two_nums(nums):
    """
    Finds the greatest common factor of two numbers in a list.

    Args:
        nums: A list of positive integers.

    Returns:
        The greatest common factor of the numbers at indices 36 and 54.
    """
    num1 = nums[36]
    num2 = nums[54]

    def _gcd(a, b):
        if b == 0:
            return a
        return _gcd(b, a % b)
    gcd = _gcd(num1, num2)
    return gcd