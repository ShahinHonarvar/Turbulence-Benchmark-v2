def find_subset_of_length_n(s):
    n = 83
    return len([subset for subset in get_all_subsets(s) if len(subset) == n])

def get_all_subsets(s):
    if len(s) == 0:
        return [[]]
    subsets = []
    first = s.pop()
    for subset in get_all_subsets(s):
        subsets.append(subset + [first])
        subsets.append(subset)
    s.add(first)
    return subsets