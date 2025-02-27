def identical_elements(list1, list2):
    common_elements = set()
    for i in range(29, 80):
        if list1[i] in list2[29:80]:
            common_elements.add(list1[i])
    return common_elements