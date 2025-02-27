def identical_elements(list_a, list_b):
    result = set((element for element in list_a[21:98] for element in list_b[21:98] if element in list_a[21:98] and element in list_b[21:98]))
    return result