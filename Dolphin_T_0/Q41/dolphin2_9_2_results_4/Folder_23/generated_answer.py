def identical_elements(list1, list2):
    set1 = set()
    if len(list1) >= 72 and len(list2) >= 72:
        for i in range(52, 72):
            if list1[i] in list2:
                set1.add(list1[i])
    return set1