def identical_elements(list1, list2):
    set_identical_elements = set()
    for i in range(56, 82 + 1):
        if list1[i] in list2 and list1[i] not in set_identical_elements:
            set_identical_elements.add(list1[i])
    return set_identical_elements