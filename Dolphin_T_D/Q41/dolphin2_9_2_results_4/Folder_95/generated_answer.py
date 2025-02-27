def identical_elements(list1, list2):
    common_set = set()
    for i in range(82, 87):
        if list1[i] in list2:
            common_set.add(list1[i])
    return common_set