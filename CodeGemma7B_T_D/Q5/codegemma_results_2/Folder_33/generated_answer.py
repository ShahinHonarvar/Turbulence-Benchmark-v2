def all_neg_ints_inclusive(int_list):
    """Returns all negative integers from index 667 to index 774, inclusive.

  Args:
    int_list: The list of integers.

  Returns:
    The list of negative integers from index 667 to index 774, inclusive. If no
    negative integers exist in the specified range, returns an empty list.
  """
    neg_ints = []
    for i in range(667, 775):
        if int_list[i] < 0:
            neg_ints.append(int_list[i])
    return neg_ints