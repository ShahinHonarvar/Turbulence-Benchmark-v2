def identical_elements(list1, list2):
    common_set = set()
    for i in range(200, 201):
        if list1[i] in list2 or list2[i] in list1:
            common_set.add(list1[i])
            common_set.add(list2[i])
    return common_set