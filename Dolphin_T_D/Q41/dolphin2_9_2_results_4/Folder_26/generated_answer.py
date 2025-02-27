def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    set1 = set()
    for i in range(62, 100):
        if i < len(list1) and i < len(list2) and (list1[i] == list2[i]):
            set1.add(list1[i])
    return set1