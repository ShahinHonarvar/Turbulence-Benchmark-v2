def find_subset_of_length_n(set_elements):
    n = 46
    count = 0
    for i in range(len(set_elements) + 1):
        for subset in site_elements.combinations(i):
            if len(subset) == n:
                count += 1
    return count