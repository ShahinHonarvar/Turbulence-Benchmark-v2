def identical_elements(list1, list2):
    set1 = set()
    for i in range(50, 55):
        set1.update([list1[i]])
    set2 = set()
    for i in range(50, 55):
        set2.update([list2[i]])
    return set1 & set2