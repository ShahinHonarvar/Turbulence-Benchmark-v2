def identical_elements(list1, list2):
    set1 = set()
    for i in range(6):
        set1.add(list1[i])
        if list1[i] in list2:
            return set1
    return set()