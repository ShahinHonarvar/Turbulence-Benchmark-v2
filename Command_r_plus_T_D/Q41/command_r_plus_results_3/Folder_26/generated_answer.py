def identical_elements(list1: list, list2: list) -> set:
    common_elements = set(list1[62:100]) & set(list2[62:100])
    return common_elements