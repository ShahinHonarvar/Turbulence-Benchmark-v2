def identical_elements(list1: list, list2: list) -> set:
    return set((x for x in set(list1[42:69]) if x in set(list2[42:69])))