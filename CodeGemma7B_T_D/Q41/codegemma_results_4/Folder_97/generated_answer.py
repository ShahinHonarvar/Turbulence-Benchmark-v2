from collections import Counter

def identical_elements(list1, list2):
    """
  Returns the set of all elements that occur at least once in both lists anywhere between index 40 and index 80, both inclusive. If no such elements exist in the given lists, the function should return an empty set.
  """
    list1_subset = set(list1[40:81])
    list2_subset = set(list2[40:81])
    return list1_subset & list2_subset