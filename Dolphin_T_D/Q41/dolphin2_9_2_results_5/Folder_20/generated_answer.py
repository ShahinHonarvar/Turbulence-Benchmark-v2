def identical_elements(list1, list2):
    set1 = set()
    for i in range(56, 67):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                set1.add(list1[i])
    return set1