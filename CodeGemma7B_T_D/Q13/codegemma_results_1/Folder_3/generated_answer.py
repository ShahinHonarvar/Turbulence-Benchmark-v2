def find_second_largest_num(num_list):
    """
  This function takes one argument, a list of distinct numbers, as input and returns the second largest element from the index 62 to the index 92, both inclusive. If there is no such element, the function should return 'None'.

  Args:
    num_list: A list of distinct numbers.

  Returns:
    The second largest element from the index 62 to the index 92, both inclusive. If there is no such element, the function should return 'None'.
  """
    num_list_copy = num_list[:]
    num_list_copy.sort(reverse=True)
    if len(num_list_copy) - 1 >= 30:
        return num_list_copy[30]
    else:
        return 'None'