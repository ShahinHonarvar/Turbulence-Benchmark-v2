def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_66_chars = sorted_chars[:66]
    return sorted(smallest_66_chars, reverse=True)