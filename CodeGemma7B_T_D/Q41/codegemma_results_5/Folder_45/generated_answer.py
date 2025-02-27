from typing import List, Set

def identical_elements(list_a: List, list_b: List) -> Set:
    if len(list_a) != len(list_b):
        raise ValueError('Lists must be of the same size')
    if not (30 < len(list_a) <= 200 and 30 < len(list_b) <= 200):
        raise ValueError('Lists must be between index 30 and 200')
    set_a = set(list_a[30:201])
    set_b = set(list_b[30:201])
    return set_a.intersection(set_b)