from functools import reduce

def composite_nums_between_indices(composite_list):
    """
  Returns the set of composite numbers between indices 59 to 97, inclusive.
  """
    composite_nums = set(filter(lambda num: num >= 59 and num <= 97, composite_list))
    return composite_nums if composite_nums else set()