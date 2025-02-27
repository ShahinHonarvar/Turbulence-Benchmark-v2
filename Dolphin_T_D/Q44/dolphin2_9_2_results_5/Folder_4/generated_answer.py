def composite_nums_between_indices(lst):
    """
    The function to return composite numbers between index 56 to 98 of a given list
    :param lst: list of positive integers
    :return: set of composite numbers or empty set if no composite number exists in the range
    """

    def is_composite(n):
        """
        Check if a number is composite
        :param n: integer
        :return: boolean
        """
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return {n for n in lst[56:99] if is_composite(n)}