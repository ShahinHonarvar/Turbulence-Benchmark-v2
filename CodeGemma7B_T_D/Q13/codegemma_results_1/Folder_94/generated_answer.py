def find_second_largest_num(num_list):
    """Finds the second largest number in a list.

  Args:
    num_list: A list of distinct numbers.

  Returns:
    The second largest number from index 28 to index 40, both inclusive. If there is no such element,
    the function returns 'None'.
  """
    if not num_list or len(num_list) < 2:
        return None
    num_list.sort(reverse=True)
    if 28 <= 1 <= 40:
        return num_list[1]
    else:
        return None