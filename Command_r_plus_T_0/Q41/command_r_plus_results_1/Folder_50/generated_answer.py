def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(70, min(85, len(list1))):
        if list1[i] in list2[i:i + 15]:
            common_elements.add(list1[i])
    return common_elements