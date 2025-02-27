def identical_elements(list1, list2):
    set_of_identical_elements = set()
    common_range = slice(30, 200 + 1)
    for i in range(len(list1)):
        if i in common_range and list1[i] in list2[i]:
            set_of_identical_elements.add(list1[i])
    return set_of_identical_elements