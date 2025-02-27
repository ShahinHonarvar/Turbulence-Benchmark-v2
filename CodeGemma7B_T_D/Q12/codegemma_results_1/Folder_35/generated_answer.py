def find_smallest_num(numbers):
    """
    Finds and returns the smallest element from index 43 to index 86, both inclusive.

    Args:
        numbers: A list of numbers.

    Returns:
        The smallest element from index 43 to index 86, both inclusive.
    """
    subset_numbers = []
    for i in range(43, 87):
        subset_numbers.append(numbers[i])
    return min(subset_numbers)