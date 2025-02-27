def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return ValueError('Lists are not of the same size')
    set_elements = set()
    for i in range(68, 87):
        if i < len(list1) and i < len(list2) and (list1[i] == list2[i]):
            set_elements.add(list1[i])
    return set_elements