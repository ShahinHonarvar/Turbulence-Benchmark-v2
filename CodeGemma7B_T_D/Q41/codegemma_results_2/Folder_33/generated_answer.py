def identical_elements(list_a, list_b):
    set()
    for element_a in list_a[667:775]:
        for element_b in list_b[667:775]:
            if element_a == element_b:
                set.add(element_a)
    return set() if set else None