def identical_elements(list1, list2):
    common = set()
    for i in range(40, 81):
        if i < len(list1) and i < len(list2) and (list1[i] == list2[i]):
            common.add(list1[i])
    return common