def identical_elements(list1, list2):
    common_elements = set()
    for i in range(1, 9):
        if i in range(len(list1)) and i in range(len(list2)):
            if list1[i] in list2:
                common_elements.add(list1[i])
            if list2[i] in list1:
                common_elements.add(list2[i])
    return common_elements