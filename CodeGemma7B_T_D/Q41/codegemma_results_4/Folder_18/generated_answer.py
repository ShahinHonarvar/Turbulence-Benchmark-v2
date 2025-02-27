def identical_elements(list_1, list_2):
    return set((l for i, l in enumerate(zip(list_1, list_2)) if i in range(35, 50)))