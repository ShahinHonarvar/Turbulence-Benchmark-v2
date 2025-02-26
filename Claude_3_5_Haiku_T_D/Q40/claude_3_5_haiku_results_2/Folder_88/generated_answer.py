def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    return sorted_chars[:84] if len(sorted_chars) >= 84 else sorted_chars