def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    return sorted_chars[:72] if len(sorted_chars) >= 72 else sorted_chars