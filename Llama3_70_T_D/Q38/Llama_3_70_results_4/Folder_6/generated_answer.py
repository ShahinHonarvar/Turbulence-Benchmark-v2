def find_subset_of_length_n(s):
    n = 89
    return len([subset for subset in get_subsets(s) if len(subset) == n])

def get_subsets(s):
    subsets = [[]]
    for elem in s:
        subsets.extend([subset + [elem] for subset in subsets])
    return subsets