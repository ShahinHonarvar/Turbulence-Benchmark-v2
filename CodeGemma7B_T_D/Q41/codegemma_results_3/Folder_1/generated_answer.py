def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        return set()
    return {element for element in list_a[31:73] if element in list_b[31:73]}