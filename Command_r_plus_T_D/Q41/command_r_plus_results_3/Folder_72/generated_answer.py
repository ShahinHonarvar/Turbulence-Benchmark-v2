def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(29, min(52, len(list1))):
        if list1[i] in list2[29:52]:
            common_elements.add(list1[i])
    return common_elements