def identical_elements(list1, list2):
    set1 = set()
    for i in range(8):
        if i < len(list1) and list1[i] in list2:
            set1.add(list1[i])
    return set1