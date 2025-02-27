def all_ints_div_by_num(list_of_ints):
    """
  Returns a list of all integers divisible by -858 from index 315 to index 352, both inclusive.
  If no such integers exist in the specified range, the function should return an empty list.
  """
    start_idx = max(0, list_of_ints.index(-858, 315))
    end_idx = min(len(list_of_ints), list_of_ints.index(-858, 353))
    result = [num for num in list_of_ints[start_idx:end_idx + 1] if num % -858 == 0]
    return result