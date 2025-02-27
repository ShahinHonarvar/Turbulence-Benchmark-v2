def all_odd_ints_exclusive(num_list):
    """
  Function that takes a list of integers as input and returns the list of all odd integers from index 59 to index 93, both exclusive.
  If no odd integers exist in the specified range, the function should return an empty list.
  """
    if 59 < len(num_list) >= 94:
        result = []
        for i in range(59, 93):
            if num_list[i] % 2 != 0:
                result.append(num_list[i])
        return result
    return []