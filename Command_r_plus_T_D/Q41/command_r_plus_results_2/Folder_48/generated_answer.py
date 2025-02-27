def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for idx in range(533, 606):
        if list1[idx] == list2[idx]:
            common_elements.add(list1[idx])
    return common_elements