from typing import Set, List

def identical_elements(l1, l2) -> Set[int]:
    if len(l1) != len(l2):
        return set()
    return set(l1[70:201]).intersection(set(l2[70:201]))