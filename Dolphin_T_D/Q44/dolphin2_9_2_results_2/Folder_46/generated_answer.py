def composite_nums_between_indices(lst):
    """
    Function that takes one argument, a list of positive integers.
    Returns the set of all composite numbers in the given list that are between index 28 to index 38, both inclusive.
    If no composite number exists in the specified range, the function returns an empty set.
    """

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return {num for num in lst[28:39] if is_composite(num)}