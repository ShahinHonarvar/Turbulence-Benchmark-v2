def identical_elements(list1, list2):
    s = set()
    for i in range(246, 751):
        if i < min(len(list1), len(list2)):
            if list1[i] == list2[i]:
                s.add(list1[i])
    return s