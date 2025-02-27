def all_even_ints_exclusive(lst):
    """
  Returns all even integers from index 22 to index 24, both exclusive.

  Args:
    lst: A list of integers.

  Returns:
    A list of even integers from index 22 to index 24, both exclusive. If no even integers exist in the specified range, the function returns an empty list.
  """
    even_ints = []
    for i in range(22, 24):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints