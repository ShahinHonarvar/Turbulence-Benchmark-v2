def identical_elements(list1, list2):
    common_elements = set()
    for i in range(25, 88):
        if list1[i] in list2[25:88]:
            common_elements.add(list1[i])
    return common_elements