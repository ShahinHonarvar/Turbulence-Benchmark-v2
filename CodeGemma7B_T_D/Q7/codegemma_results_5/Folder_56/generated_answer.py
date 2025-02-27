def all_even_ints_inclusive(nums):
    """
    Returns a list of all even integers from index 0 to index n, inclusive.
    If no even integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums if num % 2 == 0]