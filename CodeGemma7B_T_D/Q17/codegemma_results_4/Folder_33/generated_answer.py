from math import gcd

def all_ints_div_by_both_two_nums(num_list):
    """Returns a list of integers divisible by both -722 and -731 from index 281 to 694, both inclusive.
  """
    result = []
    for i in range(281, 695):
        if gcd(-722, num_list[i]) == 1 and gcd(-731, num_list[i]) == 1:
            result.append(num_list[i])
    if not result:
        result = []
    return result