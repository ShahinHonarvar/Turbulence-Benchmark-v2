def return_n_smallest_chars(s):
    sorted_chars = sorted(list(set(s)))
    return sorted_chars[:29] if len(sorted_chars) >= 29 else sorted_chars