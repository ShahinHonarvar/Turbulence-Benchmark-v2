def identical_elements(list1: list, list2: list) -> set:
    common_elements = set(list1[70:85]) & set(list2[70:85])
    return common_elements