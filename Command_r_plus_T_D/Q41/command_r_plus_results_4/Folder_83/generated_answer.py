def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(90, 201):
        if list1[i] in list2[90:201] and list1[i] not in common_elements:
            common_elements.add(list1[i])
    return common_elements