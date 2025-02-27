def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        return set()
    result = set((element for element in list_a[4:5] if element in list_b[4:5]))
    return result or set()