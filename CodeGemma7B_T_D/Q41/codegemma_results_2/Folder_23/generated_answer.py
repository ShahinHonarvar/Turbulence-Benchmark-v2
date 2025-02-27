def identical_elements(list1, list2):
    set1 = set()
    set2 = set()
    for i in range(52, 72):
        if list1[i] == list2[i]:
            set1.add(list1[i])
            set2.add(list2[i])
    set1.intersection(set2)
    return set1