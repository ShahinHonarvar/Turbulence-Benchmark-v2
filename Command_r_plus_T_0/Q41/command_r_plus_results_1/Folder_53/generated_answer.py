def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(200, min(len(list1), len(list2)) + 1):
        if list1[i - 201] in list2[i - 201:i]:
            common_elements.add(list1[i - 201])
    return common_elements