def all_neg_ints_exclusive(lst):
    """
  Returns a list of all negative integers from index 27 to index 34, both exclusive.
  If no negative integers exist in the specified range, the function should return an empty list.
  """
    neg_ints = []
    for i in range(27, 34):
        if lst[i] < 0:
            neg_ints.append(lst[i])
    return neg_ints