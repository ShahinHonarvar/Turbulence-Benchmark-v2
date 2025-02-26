def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)[:23]
    return sorted_chars