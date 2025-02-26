def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s))
    return sorted_chars[:24] if len(sorted_chars) >= 24 else sorted_chars