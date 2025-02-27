def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    common_elements = set()
    for i in range(667, 775):
        if list1[i] in list2 and list1[i] not in common_elements:
            common_elements.add(list1[i])
        elif list1[i] not in list2 and list2[i] in common_elements:
            common_elements.remove(list2[i])
    return common_elements