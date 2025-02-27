def identical_elements(list1, list2):
    common = set()
    for i in range(30, 201):
        if i < len(list1) and i < len(list2) and (list1[i] in list2) and (list2[i] in list1):
            common.add(list1[i])
    return common