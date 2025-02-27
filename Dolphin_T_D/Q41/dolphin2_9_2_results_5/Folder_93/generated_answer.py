def identical_elements(list1, list2):
    common_set = set()
    for index in range(75, 95):
        if list1[index] == list2[index]:
            common_set.add(list1[index])
    return common_set