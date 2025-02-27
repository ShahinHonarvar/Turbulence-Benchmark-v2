def find_second_smallest_num(num_list):
    """
  Finds the second smallest number from index 52 to index 71, inclusive.

  Args:
    num_list: A list of distinct numbers.

  Returns:
    The second smallest number from index 52 to index 71, inclusive. If there is no such an element, the function returns 'None'.
  """
    num_list.sort()
    if len(num_list) <= 71 or num_list[71] == num_list[51]:
        return 'None'
    return num_list[52]