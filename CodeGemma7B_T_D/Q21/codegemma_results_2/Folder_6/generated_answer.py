from index 13 to index 63. The list is empty if no such elements

def all_ints_div_by_num(int_list):
    """
  this function returns a list of all integers divisible by the number
  exist.
  """
    result = []
    for number in int_list[13:64]:
        if number % 46 == 0:
            result.append(number)
    return result