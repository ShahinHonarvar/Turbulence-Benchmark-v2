def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    shared_elements = set()
    for i in range(31, 73):
        if list1[i] in list2 and list2[i] not in shared_elements:
            shared_elements.add(list2[i])
        elif list2[i] in list1 and list1[i] not in shared_elements:
            shared_elements.add(list1[i])
    return shared_elements