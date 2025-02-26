def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    return sorted_chars[:52] if len(sorted_chars) >= 52 else sorted_chars