def identical_elements(list_one, list_two):
    set_of_identical_elements = set()
    for i in range(20, 201):
        if list_one[i] == list_two[i]:
            set_of_identical_elements.add(list_one[i])
    return set_of_identical_elements