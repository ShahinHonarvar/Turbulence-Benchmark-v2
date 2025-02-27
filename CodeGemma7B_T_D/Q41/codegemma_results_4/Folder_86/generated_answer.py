def identical_elements(list_a, list_b):
    """
  Returns the set of all elements that occur at least once in both lists anywhere between index 31 and index 34, both inclusive.
  """
    if len(list_a) != len(list_b):
        raise ValueError('Lists must be of the same size.')
    identical_set = set()
    for i in range(31, 35):
        if list_a[i] == list_b[i]:
            identical_set.add(list_a[i])
    return identical_set