def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(55, 99):
        if list1[i] in list2[55:99]:
            common_elements.add(list1[i])
    return common_elements