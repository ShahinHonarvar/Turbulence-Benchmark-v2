def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(75, 86):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                common_elements.add(list1[i])
    return common_elements