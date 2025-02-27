from typing import List

def identical_elements(list1: List[int], list2: List[int]) -> set[int]:
    return set(list1[25:60]) & set(list2[25:60])