def all_ints_div_by_num(num_list):
    """
  This function returns the list of all integers divisible by 3 from index 30 to index 30, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for num in num_list[30:31]:
        if num % 3 == 0:
            result.append(num)
    return result