def identical_elements(list1, list2):
    common_elements = set()
    for i in range(262, 747):
        if list1[i] in list2[262:747] and list1[i] not in common_elements:
            common_elements.add(list1[i])
    return common_elements