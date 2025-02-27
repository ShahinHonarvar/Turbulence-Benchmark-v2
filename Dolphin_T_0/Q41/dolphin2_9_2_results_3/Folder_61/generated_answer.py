def identical_elements(list1, list2):
    set1 = set()
    for i in range(7):
        if list1[i] in list2 and list1[i] not in set1:
            set1.add(list1[i])
    return set1