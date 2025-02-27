def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for index in range(20, 201):
        if index < len(list1) and index < len(list2) and (list1[index] == list2[index]):
            common_elements.add(list1[index])
    return common_elements