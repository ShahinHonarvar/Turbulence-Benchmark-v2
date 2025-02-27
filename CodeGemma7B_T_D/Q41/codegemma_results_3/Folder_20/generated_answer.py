def identical_elements(list_a, list_b):
    set_identical_elements = set(list_a[56:67]).intersection(set(list_b[56:67]))
    return set_identical_elements if set_identical_elements else set()