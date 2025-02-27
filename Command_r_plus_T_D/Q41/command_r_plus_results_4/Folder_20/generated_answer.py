def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(56, min(67, len(list1), len(list2))):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements