def find_subset_of_length_n(elements):
    result = 0
    for subset in combinations(elements, 24):
        result += 1
    return result