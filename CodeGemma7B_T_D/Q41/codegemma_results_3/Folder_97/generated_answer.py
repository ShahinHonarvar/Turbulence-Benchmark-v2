from typing import List, Set

def identical_elements(list1: List[int], list2: List[int]) -> Set[int]:
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 40 and index 80, both inclusive.

    Args:
        list1: The first list.
        list2: The second list.

    Returns:
        An empty set if no elements are found.
    """
    return set((x for x in list1[40:81] if x in list2[40:81]))