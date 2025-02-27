def all_even_ints_exclusive(lst):
    """
  Return all even integers from index 28 to index 49, both exclusive.

  Args:
    lst: A list of integers.

  Returns:
    A list of even integers from index 28 to index 49, both exclusive, or an empty list if no even integers exist in the specified range.
  """
    if lst[28:50] and all((num % 2 == 0 for num in lst[28:50])):
        return lst[28:50]
    return []