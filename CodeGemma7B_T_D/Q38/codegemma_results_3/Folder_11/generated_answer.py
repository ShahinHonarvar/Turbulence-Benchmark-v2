def find_subset_of_length_n(set):
    count = 0
    for item in set:
        if len(item) == 77:
            count += 1
    return count