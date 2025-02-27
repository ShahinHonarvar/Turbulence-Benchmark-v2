def all_ints_div_by_both_two_nums(int_list):
    """
      Returns a list of all integers divisible by both 1 and -1 from index 0 to index 0, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
      Args:
        int_list: A list of integers.
      Returns:
        A list of integers divisible by both 1 and -1 from index 0 to index 0, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
      """
    if not int_list:
        return []
    divisible_ints = []
    for int in int_list:
        if int % 1 == 0 and int % -1 == 0:
            divisible_ints.append(int)
    return divisible_ints