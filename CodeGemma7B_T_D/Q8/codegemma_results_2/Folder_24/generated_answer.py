def all_even_ints_exclusive(nums):
    """
    Returns the list of all even integers from index 13 to index 66, both exclusive.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of even integers from index 13 to index 66, both exclusive. If no even integers exist in the specified range, the function should return an empty list.
    """
    even_ints = [n for n in nums if n % 2 == 0]
    if len(even_ints) == 0:
        return []
    else:
        return even_ints[13:66]