def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(3, min(len(list1), 6)):
        if list1[i] in list2[3:6]:
            common_elements.add(list1[i])
    return common_elements