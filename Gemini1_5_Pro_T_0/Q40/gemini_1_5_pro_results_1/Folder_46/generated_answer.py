def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s))
    return sorted(sorted_chars[:54], reverse=True)