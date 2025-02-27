from math import gcd

def gcf_three_nums(a):
    """Calculates the greatest common factor of the elements at indices 90, 84 and 47 in a list.

  Args:
    a: A list of positive integers.

  Returns:
    The greatest common factor of the elements at indices 90, 84 and 47.
  """
    element_90 = a[90]
    element_84 = a[84]
    element_47 = a[47]
    gcf = gcd(element_90, element_84)
    gcf = gcd(gcf, element_47)
    return gcf