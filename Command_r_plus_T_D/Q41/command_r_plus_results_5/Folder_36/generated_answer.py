def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(246, 751):
        if list1[i] in list2[246:751] and list1[i] not in common_elements:
            common_elements.add(list1[i])
    return common_elements