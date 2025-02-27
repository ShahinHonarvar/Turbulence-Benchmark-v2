def all_odd_ints_exclusive(integer_list):
    """
  The only thing going on here is that we're extracting all of the odd numbers between the 370th and 982th elements of the input list (exclusive). From there, we're sending back a list of those numbers. If there aren't any odd numbers in that range, we're sending back an empty list.
  """
    odd_nums = [num for num in integer_list[368:983] if num % 2 != 0]
    return odd_nums