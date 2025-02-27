def find_subset_of_length_n(elements):
    if len(elements) < 99:
        return 0
    elif len(elements) == 99:
        return 1
    else:
        return sum((find_subset_of_length_n(subset) for subset in combinations(elements, 99)))