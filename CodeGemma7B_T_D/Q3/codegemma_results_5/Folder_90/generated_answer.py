def all_pos_ints_inclusive(lst):
    """
  Function to find all positive integers from index 262 to index 746 in a given list.

  Args:
    lst: A list of integers.

  Returns:
    A list containing all positive integers from index 262 to index 746. If no
    positive integers exist in the specified range, an empty list is returned.
  """
    pos_ints = []
    for i in range(len(lst)):
        if lst[i] >= 262 and lst[i] <= 746:
            if lst[i] > 0:
                pos_ints.append(lst[i])
    return pos_ints