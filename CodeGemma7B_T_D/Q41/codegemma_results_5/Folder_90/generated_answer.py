from typing import Set

def identical_elements(list0: list, list1: list) -> Set:
    new_set = set()
    for i in range(262, 746):
        if list0[i] in list1 and list1[i] in list0:
            new_set.add(list0[i])
    return new_set