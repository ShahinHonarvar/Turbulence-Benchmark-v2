def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    return sorted_chars[:68] if len(sorted_chars) >= 68 else sorted_chars