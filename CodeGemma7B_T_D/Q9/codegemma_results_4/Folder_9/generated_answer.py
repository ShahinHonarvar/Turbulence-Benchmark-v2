def all_odd_ints_inclusive(list_of_ints):
    """
  Returns a list of all odd integers from index 70 to index 200, both inclusive.

  Args:
    list_of_ints: A list of integers.

  Returns:
    A list of odd integers from index 70 to index 200, both inclusive. If no odd integers exist in the specified range, an empty list is returned.
  """
    odd_ints = [n for n in list_of_ints if n % 2 != 0]
    filtered_ints = [n for n in odd_ints if n >= 70 and n <= 200]
    if filtered_ints:
        return filtered_ints
    else:
        return []