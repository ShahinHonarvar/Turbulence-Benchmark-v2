def identical_elements(list1: list, list2: list) -> set:
    common_elements = set(list1[310:371]) & set(list2[310:371])
    return common_elements