def identical_elements(list1, list2):
    set1 = set()
    for i in range(16, 746):
        if list1[i] == list2[i]:
            set1.add(list1[i])
    return set1