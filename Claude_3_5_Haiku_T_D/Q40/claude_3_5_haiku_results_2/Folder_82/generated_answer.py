def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s))
    return sorted_chars[:60] if len(sorted_chars) >= 60 else sorted_chars