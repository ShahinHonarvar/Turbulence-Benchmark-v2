def identical_elements(list1, list2):
    set1 = set()
    for i in range(42, 69):
        if i < len(list1) and i < len(list2):
            set1.add(list1[i])
            set1.add(list2[i])
    return set1