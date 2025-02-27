from typing import List

def identical_elements(list1: List[int], list2: List[int]) -> set[int]:
    return set((i for i in list1[32:36] if i in list2[32:36]))