def composite_nums_between_indices(nums):
    """
    Identify composite numbers between indices 111 to 111, inclusive, in a list of positive integers.
    """

    def is_composite(n):
        """
        Check if a number n is composite.
        """
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    composite_nums = set(filter(is_composite, nums[111:112]))
    return composite_nums