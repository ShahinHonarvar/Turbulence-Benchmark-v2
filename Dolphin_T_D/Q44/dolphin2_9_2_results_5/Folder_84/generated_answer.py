def composite_nums_between_indices(nums):
    """
    Function to return composite numbers between the indices 30 and 48, inclusive.
    @param nums: list of positive integers
    @return: set of composite numbers or empty set
    """

    def is_composite(num):
        """
        Helper function to check if a number is composite
        @param num: integer
        @return: boolean
        """
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return set(filter(is_composite, nums[30:49]))