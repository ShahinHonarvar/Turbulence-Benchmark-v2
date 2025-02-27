def identical_elements(lst1, lst2):
    """
          Returns the set of all elements that occur at least once in both lists anywhere between index 22 and index 50, both inclusive. If no such elements exist in the given lists, the function should return an empty set.
          """
    lst1_elements = lst1[22:51]
    lst2_elements = lst2[22:51]
    result = lst1_elements.intersection(lst2_elements)
    if result == set():
        return set()
    return result