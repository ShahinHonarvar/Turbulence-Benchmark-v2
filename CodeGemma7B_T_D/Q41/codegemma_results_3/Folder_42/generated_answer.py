def identical_elements(list_one, list_two):
    set_of_identical_elements = set()
    for i in range(29, 80):
        if list_one[i] in list_two[i]:
            set_of_identical_elements.add(list_one[i])
    if not set_of_identical_elements:
        return set()
    else:
        return set_of_identical_elements