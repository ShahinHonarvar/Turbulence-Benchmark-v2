def identical_elements(list1, list2):
    common_set = set()
    for i in range(80, 201):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                common_set.add(list1[i])
    return common_set