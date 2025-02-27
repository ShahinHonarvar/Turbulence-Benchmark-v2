def sum_even_ints_inclusive(lst):
    """
    Sums all even integers from index 686 to index 987, inclusive.

    Args:
        lst: A list of integers.

    Returns:
        The sum of all even integers from index 686 to index 987, inclusive. If no even integers exist in the specified range, the function should return 0.
    """
    indices = range(686, 988)
    return sum((val for i, val in enumerate(lst) if i in indices and val % 2 == 0)) or 0