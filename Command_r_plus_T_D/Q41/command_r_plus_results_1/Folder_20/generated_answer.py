def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(56, min(67, len(list1))):
        if list1[i] in list2[56:67]:
            common_elements.add(list1[i])
    return common_elements