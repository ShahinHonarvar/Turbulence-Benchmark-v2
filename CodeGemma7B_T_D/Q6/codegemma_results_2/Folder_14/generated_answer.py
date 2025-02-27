def all_neg_ints_exclusive(nums):
    """
            The indices in the specified range are 1 (inclusive) to 7 (exclusive).
            """
    return [num for num in nums if num < 0 and 1 <= abs(num) < 7]