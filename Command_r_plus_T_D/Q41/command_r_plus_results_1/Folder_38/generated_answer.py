def identical_elements(list1: list, list2: list) -> set:
    common_elements = set(list1[22:64]) & set(list2[22:64])
    return common_elements