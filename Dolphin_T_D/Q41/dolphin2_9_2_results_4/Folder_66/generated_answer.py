def identical_elements(list1, list2):
    set = set()
    for i in range(50, 55):
        if list1[i] in list2:
            set.add(list1[i])
    return set