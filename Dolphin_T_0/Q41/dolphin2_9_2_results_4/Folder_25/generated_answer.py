def identical_elements(list1, list2):
    set1 = set()
    for i in range(29, 94):
        if list1[i] == list2[i]:
            set1.add(list1[i])
    return set1 if set1 else set()