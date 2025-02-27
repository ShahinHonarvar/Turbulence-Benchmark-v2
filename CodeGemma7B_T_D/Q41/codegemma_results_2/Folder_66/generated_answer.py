def identical_elements(list_a, list_b):
    set_of_identical_elements = set()
    for index in range(50, 55):
        if list_a[index] in list_b and list_a[index] not in set_of_identical_elements:
            set_of_identical_elements.add(list_a[index])
    return set_of_identical_elements