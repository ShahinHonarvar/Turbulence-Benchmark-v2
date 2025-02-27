def identical_elements(list1, list2):
    common_elements = set()
    for i in range(37, 77):
        if list1[i] in list2[37:77]:
            common_elements.add(list1[i])
    return common_elements