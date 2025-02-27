def identical_elements(list_a, list_b):
    set_of_common_elements = set()
    for i in range(35, 50):
        if list_a[i] == list_b[i]:
            set_of_common_elements.add(list_a[i])
    return set_of_common_elements