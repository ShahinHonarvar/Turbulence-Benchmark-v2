def identical_elements(list1, list2):
    for i in range(37, 52):
        if list1[i] == list2[i]:
            identical_set.add(list1[i])
    return identical_set