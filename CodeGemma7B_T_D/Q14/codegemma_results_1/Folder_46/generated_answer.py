def find_second_smallest_num(num_list):
    """
  Finds the second smallest number from index 13 to index 68, inclusive, in a list of distinct numbers.

  Args:
    num_list: A list of distinct numbers.

  Returns:
    The second smallest number from index 13 to index 68, inclusive, or 'None' if there is no such element.
  """
    if not num_list or len(num_list) < 13 or len(num_list) > 68:
        return 'None'
    sorted_list = sorted(num_list[13:69])
    return sorted_list[1] if len(sorted_list) >= 2 else 'None'