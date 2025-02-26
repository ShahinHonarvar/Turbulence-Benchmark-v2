def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    return sorted_chars[:36] if len(sorted_chars) >= 36 else sorted_chars