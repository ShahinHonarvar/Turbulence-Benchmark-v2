from typing import Set

def identical_elements(list1: list, list2: list) -> Set:
    result = set()
    for i in range(len(list1)):
        result.update((set(l1) & set(l2) for l1, l2 in zip(list1[0:i + 1], list2[0:i + 1])))
    return result