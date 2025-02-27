def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    set1 = set()
    for i in range(20, 201):
        if i < len(list1):
            if list1[i] in list2:
                set1.add(list1[i])
    return set1