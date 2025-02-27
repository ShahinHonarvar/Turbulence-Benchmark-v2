def identical_elements(list_a, list_b):
    set_c = set()
    for i in range(31, 73):
        if list_a[i] in list_b and list_a[i] not in set_c:
            set_c.add(list_a[i])
    return set_c