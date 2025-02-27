def find_subset_of_length_n(elements, n=3):
    return set((elem for elem in elements if len(elements & set(elem)) >= n))