def identical_elements(list1: list, list2: list) -> set:
    common_elements = set(list1[31:73]) & set(list2[31:73])
    return common_elements