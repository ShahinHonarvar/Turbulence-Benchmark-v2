def identical_elements(list1, list2):
    set = set()
    for i in range(37, 77):
        if list1[i] in list2[i]:
            set.add(list1[i])
    return set