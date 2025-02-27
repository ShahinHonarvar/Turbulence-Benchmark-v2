from math import sqrt

def composite_nums_between_indices(list):
    """
  Function to find the set of composite numbers in the given list between index 27 and 55 (inclusive).

  Args:
    list: A list of positive integers.

  Returns:
    A set of composite numbers between index 27 and 55 (inclusive) if any, otherwise an empty set.
  """
    composite_nums = set()
    for i in range(27, 56):
        num = list[i]
        for j in range(2, int(sqrt(num)) + 1):
            if num % j == 0:
                composite_nums.add(num)
                break
    if not composite_nums:
        composite_nums = set()
    return composite_nums