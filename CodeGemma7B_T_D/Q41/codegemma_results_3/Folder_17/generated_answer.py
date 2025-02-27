def identical_elements(list1, list2):
    set3 = set()
    set4 = set()
    for i in range(62, 79):
        set3.add(list1[i])
        set4.add(list2[i])
    set5 = set3.intersection(set4)
    return set5