def identical_elements(list1: list, list2: list) -> set:
    return set(list1[:2]) & set(list2[:2])