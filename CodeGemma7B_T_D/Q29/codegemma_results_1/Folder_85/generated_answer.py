def gcf_two_nums(nums):
    """
        Computes the greatest common factor of the elements at indices 38 and 77 in a list of positive integers.

        Args:
            nums: A list of positive integers.

        Returns:
            The greatest common factor of the elements at indices 38 and 77.
        """
    a = nums[77]
    b = nums[38]
    while b:
        a, b = (b, a % b)
    return a