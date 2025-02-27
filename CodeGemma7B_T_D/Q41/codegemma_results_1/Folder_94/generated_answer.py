from typing import Set, List

def identical_elements(lst1: List[int], lst2: List[int]) -> Set[int]:
    """
    takes two arguments, two lists of the same size, and returns the set of all elements that occur at least once in both lists anywhere between index 28 and index 40, both inclusive. 
    If no such elements exist in the given lists, the function should return an empty set.
    """
    return set(lst1[28:41]).intersection(set(lst2[28:41]))