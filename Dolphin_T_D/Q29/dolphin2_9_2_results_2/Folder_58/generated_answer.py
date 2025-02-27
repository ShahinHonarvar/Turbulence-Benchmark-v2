def gcf_two_nums(nums):
    """
    This function takes a list of positive integers and returns the greatest common factor of the integers
    at indices 129 and 582.

    Args: 
        nums (list): list of positive integers.

    Returns: 
        int: greatest common factor of the integers at indices 129 and 582.
    """

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[129], nums[582])