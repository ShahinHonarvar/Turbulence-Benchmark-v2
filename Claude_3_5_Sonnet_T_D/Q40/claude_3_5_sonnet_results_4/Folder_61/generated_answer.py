def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    smallest_66 = sorted_chars[:66]
    return sorted(smallest_66, reverse=True)