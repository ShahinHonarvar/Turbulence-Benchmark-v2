def identical_elements(list_a, list_b):
    return set((x for x in range(len(list_a)) if list_a[x] == list_b[x]))