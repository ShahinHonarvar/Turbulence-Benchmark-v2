def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    return sorted(sorted_chars[:2], reverse=True)