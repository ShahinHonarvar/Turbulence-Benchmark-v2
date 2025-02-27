def all_ints_div_by_num(num_list):
    """
  Function to get all numbers divisible by 71 in a list from index 13 to index 68 (inclusive).

  @param num_list: List of integers.
  @return: List of integers divisible by 71.
  """
    result = []
    for i in range(13, 69):
        if num_list[i] % 71 == 0:
            result.append(num_list[i])
    return result