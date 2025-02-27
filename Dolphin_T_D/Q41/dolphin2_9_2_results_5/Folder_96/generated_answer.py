def identical_elements(list1, list2):
    set1 = set()
    for idx in range(50, 201):
        if idx < len(list1) and idx < len(list2):
            if list1[idx] in list2:
                set1.add(list1[idx])
    return set1