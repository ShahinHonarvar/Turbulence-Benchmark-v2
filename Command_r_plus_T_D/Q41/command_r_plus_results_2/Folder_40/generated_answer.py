def identical_elements(list1: list, list2: list) -> set:
    common_elements = set(list1[0:2]).intersection(set(list2[0:2]))
    return common_elements