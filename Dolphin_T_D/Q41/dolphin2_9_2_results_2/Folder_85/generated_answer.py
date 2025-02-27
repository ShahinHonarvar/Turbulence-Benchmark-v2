def identical_elements(list1, list2):
    assert len(list1) == len(list2)
    set1 = set()
    for i in range(6, 9):
        if list1[i] in list2:
            set1.add(list1[i])
    return set1