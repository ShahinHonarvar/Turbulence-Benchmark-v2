def identical_elements(list1, list2):
    set1 = set()
    for i in range(7):
        if i < len(list1) and list1[i] in list2:
            set1.add(list1[i])
        if i < len(list2) and list2[i] in list1:
            set1.add(list2[i])
    return set1