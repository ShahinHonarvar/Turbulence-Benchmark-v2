def identical_elements(list1, list2):
    set_identical_elements = set()
    index = 90
    while index <= 199:
        if list1[index] == list2[index]:
            set_identical_elements.add(list1[index])
        index += 1
    return set_identical_elements