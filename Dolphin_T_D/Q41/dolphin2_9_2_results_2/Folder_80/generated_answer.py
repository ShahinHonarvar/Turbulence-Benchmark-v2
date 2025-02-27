def identical_elements(list1, list2):
    set_elements = set()
    for i in range(64, 67):
        if list1[i] in list2:
            set_elements.add(list1[i])
    return set_elements