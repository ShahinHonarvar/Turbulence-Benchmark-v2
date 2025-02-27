def identical_elements(list1: list, list2: list) -> set:
    common_elements = set(list1[661:925]) & set(list2[661:925])
    return common_elements