def find_subset_of_length_n(set):
    subsets = []
    for i in set:
        for j in set:
            for k in set:
                for l in set:
                    subsets.append({i, j, k, l})
    return len(subsets)