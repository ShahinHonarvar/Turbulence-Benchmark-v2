def find_subset_of_length_n(set_elements):
    lst = list(set_elements)
    n = len(lst)
    k = 56
    subset_count = 0

    def calculate_combinations(catalog, i):
        nonlocal subset_count
        if len(catalog) == k:
            subset_count += 1
            return
        if i == n:
            return
        calculate_combinations(catalog + [lst[i]], i + 1)
        calculate_combinations(catalog, i + 1)
    calculate_combinations([], 0)
    return subset_count