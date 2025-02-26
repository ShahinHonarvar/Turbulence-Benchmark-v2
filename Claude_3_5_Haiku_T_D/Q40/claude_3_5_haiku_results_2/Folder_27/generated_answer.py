def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    return sorted_chars[:82] if len(sorted_chars) >= 82 else sorted_chars