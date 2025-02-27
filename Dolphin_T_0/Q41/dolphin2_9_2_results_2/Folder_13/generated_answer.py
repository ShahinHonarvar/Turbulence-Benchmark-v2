def identical_elements(list1, list2):
    set1 = set()
    if len(list1) != len(list2):
        return set1
    for i in range(25, 88):
        if i < len(list1) and list1[i] in list2:
            set1.add(list1[i])
    return set1