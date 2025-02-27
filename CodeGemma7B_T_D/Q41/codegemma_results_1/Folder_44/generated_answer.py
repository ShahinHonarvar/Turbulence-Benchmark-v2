def identical_elements(list_a, list_b):
    return {x for x in list_a[13:69] for y in list_b[13:69] if x == y}