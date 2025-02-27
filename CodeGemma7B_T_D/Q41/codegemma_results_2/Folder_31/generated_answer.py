def identical_elements(list1, list2):
    set1 = set()
    set2 = set()
    for i in range(75, 89):
        if list1[i] in list2[i]:
            set1.add(list1[i])
        if list2[i] in list1[i]:
            set2.add(list2[i])
    return set1.intersection(set2)