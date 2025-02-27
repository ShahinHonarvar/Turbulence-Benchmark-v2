def identical_elements(list_one, list_two):
    """
  Returns the set of all elements that occur at least once in both lists anywhere between index 59 and index 97, both inclusive.
  If no such elements exist in the given lists, the function should return an empty set.
  """
    result = set()
    for i in range(59, 98):
        if list_one[i] in list_two and list_two[i] in list_one:
            result.add(list_one[i])
    return result