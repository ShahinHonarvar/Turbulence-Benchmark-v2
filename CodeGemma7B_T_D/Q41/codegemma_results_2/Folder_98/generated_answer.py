def identical_elements(list1, list2):
    set_identical_elements = set()
    for i in range(0, 6):
        if list1[i] in list2[i]:
            set_identical_elements.add(list1[i])
    return set_identical_elements