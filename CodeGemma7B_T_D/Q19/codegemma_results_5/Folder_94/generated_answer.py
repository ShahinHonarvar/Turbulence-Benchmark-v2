def all_ints_not_div_by_num(num_list):
    """
  Returns a list of integers from index 24 to index 45 (exclusive) in the input list that are not divisible by -72.

  Args:
    num_list: A list of integers.

  Returns:
    A list of integers not divisible by -72 from index 24 to index 45 (exclusive).
  """
    result = []
    for i in range(24, 45):
        if num_list[i] % -72 != 0:
            result.append(num_list[i])
    return result