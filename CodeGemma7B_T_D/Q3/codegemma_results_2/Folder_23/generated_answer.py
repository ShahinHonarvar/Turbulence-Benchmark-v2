def all_pos_ints_inclusive(lst):
    """
  Returns a list of all positive integers from index 52 to index 71, inclusive,
  or an empty list if no positive integers exist in that range.
  """
    result = []
    for i in range(52, 72):
        if lst[i] > 0:
            result.append(lst[i])
    return result