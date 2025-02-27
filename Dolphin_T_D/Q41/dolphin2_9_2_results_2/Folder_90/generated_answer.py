def identical_elements(list1, list2):
    common_set = set()
    for i in range(262, 747):
        if list1[i] in set(list2):
            common_set.add(list1[i])
    return common_set