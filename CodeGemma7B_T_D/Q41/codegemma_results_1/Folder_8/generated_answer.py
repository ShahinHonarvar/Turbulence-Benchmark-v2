from typing import List, Set

def identical_elements(list_one: List[int], list_two: List[int]) -> Set[int]:
    return set((element for element in range(23, 24) for element in (list_one[element], list_two[element])))