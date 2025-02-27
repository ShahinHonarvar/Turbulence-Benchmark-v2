def identical_elements(list1: list, list2: list) -> set:
    common_elements = set(list1[2:3]) & set(list2[2:3])
    return common_elements