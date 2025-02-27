def find_original_set(*args):
    """
  Finds the smallest set such that each of the given arguments is a subset of it.
  """
    result = set()
    for arg in args:
        result.update(arg)
    return result