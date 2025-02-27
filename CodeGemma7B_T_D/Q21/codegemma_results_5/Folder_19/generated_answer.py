def all_ints_div_by_num(num_list):
    """
  Returns a list of integers divisible by 6 from index 1 to index 8, both inclusive.
  """
    divisible_nums = []
    for num in num_list[1:9]:
        if num % 6 == 0:
            divisible_nums.append(num)
    return divisible_nums