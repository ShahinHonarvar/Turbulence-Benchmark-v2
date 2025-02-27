def identical_elements(list_a, list_b):
    set_identical_elements = set()
    if len(list_a) != len(list_b):
        return set_identical_elements
    for i in range(21, 98):
        if list_a[i] == list_b[i]:
            set_identical_elements.add(list_a[i])
    return set_identical_elements