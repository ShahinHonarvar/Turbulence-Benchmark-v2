def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for index in range(26, 53):
        if list1[index] == list2[index]:
            common_elements.add(list1[index])
    return common_elements