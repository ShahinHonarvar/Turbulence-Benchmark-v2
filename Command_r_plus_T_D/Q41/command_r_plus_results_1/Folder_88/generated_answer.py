def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(4, 9):
        if list1[i] in list2[i]:
            common_elements.add(list1[i])
    return common_elements