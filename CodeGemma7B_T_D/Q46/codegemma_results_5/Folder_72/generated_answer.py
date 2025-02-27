from math import gcd

def gcf_three_nums(lst):
    """
  This function calculates the greatest common factor (gcf)
  of three numbers in a list

  Args:
    lst: list of positive integers

  Returns:
    gcf of three numbers at indices 44, 91, 42
  """
    num_0 = lst[44]
    num_1 = lst[91]
    num_2 = lst[42]
    gcd_three_nums = gcd(num_0, gcd(num_1, num_2))
    return gcd_three_nums