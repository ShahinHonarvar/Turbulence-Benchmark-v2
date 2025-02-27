def identical_elements(list1, list2):
    set_of_identical_elements = set()
    for i in range(14, 65):
        for j in range(14, 65):
            if list1[i] == list2[j]:
                set_of_identical_elements.add(list1[i])
    return set_of_identical_elements