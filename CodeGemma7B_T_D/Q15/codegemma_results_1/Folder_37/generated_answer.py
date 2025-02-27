def sum_odd_ints_inclusive(lst):
    """
    Sums the odd integers from index 1 to index 5, inclusive.

    Args:
        lst: A list of integers.

    Returns:
        The sum of all odd integers from index 1 to index 5, inclusive. If no odd integers exist in the specified range, the function returns 0.
    """
    odd_numbers = []
    for i in range(1, 6):
        if lst[i] % 2 != 0:
            odd_numbers.append(lst[i])
    if not odd_numbers:
        return 0
    return sum(odd_numbers)