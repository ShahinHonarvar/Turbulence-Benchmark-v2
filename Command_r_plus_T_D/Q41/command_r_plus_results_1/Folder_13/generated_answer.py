def identical_elements(list1, list2):
    common_elements = set()
    for i in range(25, min(88, len(list1))):
        if list1[i] in list2[25:88]:
            common_elements.add(list1[i])
    return common_elements