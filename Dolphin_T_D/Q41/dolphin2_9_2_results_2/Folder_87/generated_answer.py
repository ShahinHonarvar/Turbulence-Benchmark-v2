def identical_elements(list1, list2):
    set_elements = set()
    for index in range(36, 47):
        if index < len(list1) and index < len(list2) and (list1[index] == list2[index]):
            set_elements.add(list1[index])
    return set_elements