def all_pos_ints_exclusive(lst):
    """
  <Write a function called 'all_pos_ints_exclusive' that takes one argument, a list of integers, and returns the list of all positive integers from index 18 to index 37, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.>
  """
    result = []
    for index in range(18, 38):
        if index >= len(lst) or lst[index] <= 0:
            continue
        result.append(index + 1)
    return result