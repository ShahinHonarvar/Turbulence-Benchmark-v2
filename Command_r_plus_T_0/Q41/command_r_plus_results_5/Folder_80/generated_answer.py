def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(64, 67):
        if list1[i] in list2[i:i + 3]:
            common_elements.add(list1[i])
    return common_elements