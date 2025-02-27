def identical_elements(list1, list2):
    set_of_identical_elements = set()
    for i in range(70, 85):
        if list1[i] == list2[i]:
            set_of_identical_elements.add(list1[i])
    return set_of_identical_elements