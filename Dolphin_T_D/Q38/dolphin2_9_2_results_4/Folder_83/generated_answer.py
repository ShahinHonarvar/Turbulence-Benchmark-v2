def count_subsets(n, elements):
    if len(elements) == n:
        return 1
    elif len(elements) < n:
        return 0
    else:
        return count_subsets(n, elements[1:]) + count_subsets(n, elements[:-1])

def find_subset_of_length_n(n, elements):
    return count_subsets(n, elements)