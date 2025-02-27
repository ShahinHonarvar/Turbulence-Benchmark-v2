def all_ints_div_by_both_two_nums(a):
    """
  The function takes one argument, a list of integers, and returns the list of all
  integers divisible by both 982 and 319 from index 306 to index 957, both inclusive.
  If no such integers exist in the specified range, the function should return an empty list.
  """
    b = a[306:958]
    if b:
        return [i for i in b if i % 982 == 0 and i % 319 == 0]
    else:
        return []