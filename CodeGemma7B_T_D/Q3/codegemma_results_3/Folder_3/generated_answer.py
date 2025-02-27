def all_pos_ints_inclusive(num_list):
    """Returns a list of all positive integers from index 62 to index 92, both inclusive.

  If no positive integers exist in the specified range, the function should return an empty list.

  Args:
    num_list: A list of integers.

  Returns:
    A list of positive integers from index 62 to index 92, both inclusive. If no
    positive integers exist in the specified range, the function should return an empty
    list.
  """
    result = []
    for i in range(62, 93):
        if i < len(num_list) and num_list[i] > 0:
            result.append(num_list[i])
    return result