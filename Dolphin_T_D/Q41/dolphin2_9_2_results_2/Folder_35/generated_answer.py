def identical_elements(list1, list2):
    set1 = []
    set2 = []
    for i in range(30, 49):
        if i < len(list1) and i < len(list2):
            set1.append(list1[i])
            set2.append(list2[i])
    return set(set1) & set(set2)