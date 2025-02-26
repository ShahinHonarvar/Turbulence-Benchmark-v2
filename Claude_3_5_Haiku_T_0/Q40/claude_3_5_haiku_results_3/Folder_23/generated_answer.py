def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    return sorted_chars[:46] if len(sorted_chars) >= 46 else sorted_chars