def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    s = set()
    for i in range(43, 52):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                s.add(list1[i])
    return s