def sum_odd_ints_inclusive(lst):
    """
    Sums all odd integers from index 42 to index 68 inclusive.

    Parameters:
    lst: A list of integers.

    Returns:
    The sum of all odd integers from index 42 to index 68, inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    total = 0
    for i in range(42, 69):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total