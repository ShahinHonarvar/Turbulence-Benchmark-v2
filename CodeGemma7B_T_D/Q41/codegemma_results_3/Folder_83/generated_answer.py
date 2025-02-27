def identical_elements(list_one, list_two):
    set_of_elements = set()
    for i in range(90, 201):
        if list_one[i] == list_two[i]:
            set_of_elements.add(list_one[i])
    return set_of_elements