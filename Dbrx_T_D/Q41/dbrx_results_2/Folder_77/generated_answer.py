from typing import List, Set

def identical_elements(list1: List, list2: List) -> Set:
    intersection = set()
    for i in range(527, 539):
        for j in range(527, 539):
            if i < len(list1) and j < len(list2) and (list1[i] == list2[j]):
                intersection.add(list1[i])
    return intersection