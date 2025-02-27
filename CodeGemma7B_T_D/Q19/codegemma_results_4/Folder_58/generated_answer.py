def all_ints_not_div_by_num(int_list):
    """
  Returns a list of integers not divisible by 840 from index 266 to index 586, both exclusive.
  Returns an empty list if no such integers exist.
  """
    return [x for x in int_list[266:586] if x % 840 != 0]