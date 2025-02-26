def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    smallest_chars = sorted_chars[:33] if len(sorted_chars) >= 33 else sorted_chars
    return sorted(smallest_chars, reverse=True)