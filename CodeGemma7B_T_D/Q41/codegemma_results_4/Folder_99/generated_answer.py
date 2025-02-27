def identical_elements(list_a, list_b):
    """
  Returns the set of all elements that occur at least once in both lists anywhere between index 310 and index 370, both inclusive.
  If no such elements exist in the given lists, the function should return an empty set.
  """
    return set((a for a, b in zip(list_a[310:371], list_b[310:371]) if a == b))