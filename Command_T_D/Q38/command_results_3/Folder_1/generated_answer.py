def find_subset_of_length_n(set):
    return 1 if set == [] else sum((1 for x in range(len(set))))