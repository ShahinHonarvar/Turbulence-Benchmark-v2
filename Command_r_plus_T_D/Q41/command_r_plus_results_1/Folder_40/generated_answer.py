def identical_elements(list1: list, list2: list) -> set:
    common_elements = set(list1[:2]) & set(list2[:2])
    return common_elements