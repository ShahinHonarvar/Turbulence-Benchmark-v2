def identical_elements(list1, list2):
    set = set()
    for index in range(56, 99):
        if list1[index] == list2[index]:
            set.add(list1[index])
    return set