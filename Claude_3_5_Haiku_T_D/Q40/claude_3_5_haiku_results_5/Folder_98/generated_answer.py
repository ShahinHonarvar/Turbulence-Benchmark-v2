def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)[:68]
    return sorted_chars