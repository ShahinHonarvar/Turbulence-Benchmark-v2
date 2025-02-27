def identical_elements(list1, list2):
    common_elements = set()
    for i in range(40, 201):
        if list1[i] in list2 and list2[i] not in common_elements:
            common_elements.add(list1[i])
        elif list2[i] in list1 and list1[i] not in common_elements:
            common_elements.add(list2[i])
    return common_elements