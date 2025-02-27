def all_ints_not_div_by_num(num_list):
    """
  Returns a list of integers not divisible by 10 from index 0 to index 9, exclusive.
  """
    sub_list = []
    for number in num_list:
        if number % 10 != 0 and 0 < number < 10:
            sub_list.append(number)
    return sub_list or []