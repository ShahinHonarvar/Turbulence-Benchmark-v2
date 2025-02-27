def identical_elements(list1, list2):
    common_elements = []
    if len(list1) == len(list2):
        for i in range(43, 52):
            if list1[i] in list2:
                common_elements.append(list1[i])
    return set(common_elements)