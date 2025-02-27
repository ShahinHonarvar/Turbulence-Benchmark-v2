def identical_elements(list1, list2):
    set1 = set()
    for i in range(25, 87 + 1):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                set1.add(list1[i])
            elif list1[i] in list2 and list2.index(list1[i]) in range(25, 87 + 1):
                set1.add(list1[i])
    return set1