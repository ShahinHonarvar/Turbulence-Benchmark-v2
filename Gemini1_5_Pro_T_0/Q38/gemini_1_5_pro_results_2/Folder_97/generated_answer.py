def find_subset_of_length_n(set_of_elements):
    n = 219
    count = 0
    for i in range(len(set_of_elements) + 1):
        for element in combinations(set_of_elements, i):
            if len(element) == n:
                count += 1
    return count