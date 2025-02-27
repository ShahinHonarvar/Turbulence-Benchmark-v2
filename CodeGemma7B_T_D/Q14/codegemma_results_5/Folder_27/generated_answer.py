def find_second_smallest_num(num_list):
    """
  Finds the second smallest number from index 25 to index 59, inclusive.

  Args:
    num_list: A list of distinct numbers.

  Returns:
    The second smallest element from index 25 to index 59, inclusive. If no element exists, returns 'None'.
  """
    if len(num_list) == 0 or len(num_list) == 1:
        return None
    num_list = sorted(num_list)
    if len(num_list) < 59:
        return None
    for i in range(25, 60):
        if i < len(num_list):
            return num_list[i]
    return None