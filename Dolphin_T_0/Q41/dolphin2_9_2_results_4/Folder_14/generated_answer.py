def identical_elements(list1, list2):
    set_elements = set()
    for i in range(5, 8):
        if list1[i] == list2[i]:
            set_elements.add(list1[i])
    return set_elements