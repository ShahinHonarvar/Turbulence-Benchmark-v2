def identical_elements(list_1, list_2):
    set_of_identical_elements = set()
    for index in range(75, 89):
        if list_1[index] == list_2[index]:
            set_of_identical_elements.add(list_1[index])
    return set_of_identical_elements