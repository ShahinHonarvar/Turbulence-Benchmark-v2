from typing import Set, List
from itertools import product

def identical_elements(list1: List[Any], list2: List[Any]) -> Set[Any]:
    """
    This function takes two lists of the same size as input and returns the set of all elements that occur at least once in both lists anywhere between index 60 and index 200, both inclusive.
    If no such elements exist in the given lists, the function should return an empty set.
    """
    return set((element for idx, element in product(range(60, 201), zip(list1, list2)) if element[0] == element[1]))