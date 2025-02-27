def find_subset_of_length_n(elements):
    if len(elements) < 88:
        return 0
    num_subsets = 0
    for i in range(len(elements) - 87):
        combination = elements[i:i + 88]
        num_subsets += 1 if len(set(combination)) == 88 else 0
    return num_subsets