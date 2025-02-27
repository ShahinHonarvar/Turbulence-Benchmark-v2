def identical_elements(list1, list2):
    elements_set = set()
    for i in range(10, 101):
        if i < len(list1) and i < len(list2) and (list1[i] == list2[i]):
            elements_set.add(list1[i])
    return elements_set