def identical_elements(list1, list2):
    common_set = set()
    for i in range(26, 53):
        if list1[i] == list2[i]:
            common_set.add(list1[i])
    return common_set